import logging
import asyncio
import heapq
import datetime

from .. import fix_engine
from .. import fix_message
from .. import fix_errors


logger = logging.getLogger(__name__)

class MessageValidatorMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accept_unknown_fields = True #set to true initially because first message drives the settings
        self.send_time_tolerance = datetime.timedelta(minutes = 2)
        self.validate_comp_ids = True
        self.validate_req_fields = True

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.__TargetCompID = self.settings['TargetCompID']
        self.__SenderCompID = self.settings['SenderCompID']
        self.__BeginString = self.settings['BeginString']

        self.accept_unknown_fields = self.settings.getboolean('AcceptUnknownFields', fallback =False)
        self.send_time_tolerance = datetime.timedelta(minutes = self.settings.get('SendingTimeTolerance', fallback =2)) 
        self.validate_comp_ids = self.settings.getboolean('ValidateCompIDs', fallback =True)
        self.validate_req_fields = self.settings.getboolean('ValidateRequiredFields', fallback =True)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(None, self.on_first_message, priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.FIRST , one_time = True)
        if self.validate_comp_ids:
            self.register_admin_callback(None, self.on_validate_message, priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.FIRST + fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.AFTER)
        if self.send_time_tolerance > datetime.timedelta(minutes=0):
            self.register_admin_callback(None, self.on_validate_sendtime, priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.FIRST + fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.AFTER)
        if self.validate_req_fields:
            self.register_admin_callback(None, self.on_validate_req_fields, priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.FIRST + fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.AFTER)
        


    async def parse_message(self, *args, **kwargs):
        try:
            msg, buffer, missed_fields =  await super().parse_message(*args, **kwargs)
            if not self.accept_unknown_fields and len(missed_fields) > 0:
                ref_tag, _ = missed_fields[0].split(fix_message.EQU,1)
                raise fix_errors.FIXInvalidMessageFieldError(msg.Header.MsgSeqNum, msg._msgtype, ref_tag, "Invalid tag number", self.message_lib.fields.SessionRejectReason.ENUM_INVALID_TAG_NUMBER)
            return msg, buffer, missed_fields
        except (asyncio.IncompleteReadError, ConnectionError) as e:
            logger.debug(f"Connection closed {e}")
            self.close_connection()
            return None, None, None
        except fix_errors.FIXRejectError as e:
            logger.error(e)
            self.application._on_error(self.session_name, e)
            curr_seq = self.store.get_current_in_seq()
            self.store.set_current_in_seq(curr_seq + 1)
            self.send_reject(curr_seq, e.RefMsgType, e.RefTagID, e.Text, e.SessionRejectReason)
            return None, None, None
        except fix_errors.FIXDropMessageError as e:
            self.application._on_error(self.session_name, e)
            return None, None, None
        except Exception as e:
            raise


    def on_first_message(self, session_name, msg):
        if not isinstance(msg, self.message_lib.fix_messages.Logon):
            raise fix_errors.FIXInvalidFirstMessage("First message not a logon")


    def on_validate_message(self, session_name, msg):
        if msg.Header.BeginString != self.__BeginString:
            error= f"Invalid BeginString [{msg.Header.BeginString}] on message, expecting [{self.__BeginString}]"
            raise fix_errors.FIXInvalidMessageError(error, wait_interval=2, send_test_msg=False)
        if msg.Header.TargetCompID != self.__SenderCompID:
            error= f"Invalid TargetCompID [{msg.Header.TargetCompID}] on message, expecting [{self.__SenderCompID}]"
            raise fix_errors.FIXBadCompIDError(msg.Header.MsgSeqNum, msg._msgtype, msg.Header.tags.TargetCompID, 
                error, self.message_lib.fields.SessionRejectReason.ENUM_COMP_ID_PROBLEM, wait_interval=2, send_test_msg=False)
        if msg.Header.SenderCompID != self.__TargetCompID:
            error= f"Invalid SenderCompID [{msg.Header.SenderCompID}] on message, expecting [{self.__TargetCompID}]"
            raise fix_errors.FIXBadCompIDError(msg.Header.MsgSeqNum, msg._msgtype, msg.Header.tags.SenderCompID, 
                error, self.message_lib.fields.SessionRejectReason.ENUM_COMP_ID_PROBLEM, wait_interval=2, send_test_msg=False)

        if msg.Header.PossDupFlag == self.message_lib.fields.PossDupFlag.ENUM_POSSIBLE_DUPLICATE and msg.Header.OrigSendingTime is None:
            raise fix_errors.RequiredTagMissingError(msg.Header.MsgSeqNum, msg._msgtype, msg.Header.tags.OrigSendingTime, 
                "Required tag missing", self.message_lib.fields.SessionRejectReason.ENUM_REQUIRED_TAG_MISSING)

    def on_validate_sendtime(self, session_name, msg):        
        send_time = datetime.datetime.strptime(msg.Header.SendingTime, self.time_format)
        if abs(datetime.datetime.utcnow() - send_time) > self.send_time_tolerance:
            raise fix_errors.FIXSendTimeAccuracyError(msg.Header.MsgSeqNum, msg._msgtype, msg.Header.tags.SendingTime, 
                 "SendingTime accuracy problem", self.message_lib.fields.SessionRejectReason.ENUM_SENDING_TIME_ACCURACY_PROBLEM,
                 wait_interval=2, send_test_msg=False)
            
    def on_validate_req_fields(self, session_name, msg):
        tag = msg.get_first_unset_required_field()
        if tag is not None:
            raise fix_errors.FIXInvalidMessageFieldError(msg.Header.MsgSeqNum, msg._msgtype, tag,  "Required tag missing", 
                    self.message_lib.fields.SessionRejectReason.ENUM_REQUIRED_TAG_MISSING)
        return None

