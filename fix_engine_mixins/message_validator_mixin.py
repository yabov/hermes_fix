import logging
import asyncio
import fix_engine
import heapq
import fix_errors
import datetime

logger = logging.getLogger(__name__)

class MessageValidatorMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.__TargetCompID = self.settings['TargetCompID']
        self.__SenderCompID = self.settings['SenderCompID']
        self.__BeginString = self.settings['BeginString']

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_callback(None, self.on_first_message, priority = fix_engine.CallbackWrapper.CALLBACK_PRIORITY.FIRST)
        self.register_callback(None, self.on_validate_message, priority = fix_engine.CallbackWrapper.CALLBACK_PRIORITY.HIGH)
        
    async def parse_message(self, *args, **kwargs):
        try:
            return await super().parse_message(*args, **kwargs)
        except (asyncio.streams.IncompleteReadError, ConnectionError) as e:
            logger.debug(f"Connection closed {e}")
            self.close_connection()
            return None
        except fix_errors.FIXGarbledMessageError as e:
            self.application.on_error(e)
            return None
        except Exception as e:
            raise


    def on_first_message(self, msg):
        if not isinstance(msg, self.message_lib.Logon):
            raise fix_errors.FIXInvalidFirstMessage("First message not a logon")
        heapq.heappop(self.call_back_register[None])


    def on_validate_message(self, msg):
        if msg.Header.BeginString != self.__BeginString:
            error= f"Invalid BeginString [{msg.Header.BeginString}] on message, expecting [{self.__BeginString}]"
            raise fix_errors.FIXInvalidMessageError(error)
        if msg.Header.TargetCompID != self.__SenderCompID:
            error= f"Invalid SenderCompID [{msg.Header.SenderCompID}] on message, expecting [{self.__TargetCompID}]"
            reject_msg = self.message_lib.Reject()
            try:
                reject_msg.RefSeqNum = msg.Header.MsgSeqNum
                reject_msg.RefMsgType = msg._msgtype
                reject_msg.RefTagID = msg.Header.tags.OrigSendingTime
                reject_msg.Text = error             
                reject_msg.SessionRejectReason = self.message_lib.SessionRejectReason.ENUM_COMPID_PROBLEM
            except:
                pass
            self.send_message(reject_msg)
            raise fix_errors.FIXBadCompIDError(error)   
        if msg.Header.SenderCompID != self.__TargetCompID:
            error= f"Invalid SenderCompID [{msg.Header.SenderCompID}] on message, expecting [{self.__TargetCompID}]"
            reject_msg = self.message_lib.Reject()
            try:
                reject_msg.RefSeqNum = msg.Header.MsgSeqNum
                reject_msg.RefMsgType = msg._msgtype
                reject_msg.RefTagID = msg.Header.tags.OrigSendingTime
                reject_msg.Text = error             
                reject_msg.SessionRejectReason = self.message_lib.SessionRejectReason.ENUM_COMPID_PROBLEM
            except:
                pass
            self.send_message(reject_msg)
            raise fix_errors.FIXBadCompIDError(error)

        self.validate_sendtime(msg)

    def validate_sendtime(self, msg):        
        send_time = datetime.datetime.strptime(msg.Header.SendingTime, self.time_format)
        if abs(datetime.datetime.utcnow() - send_time) > datetime.timedelta(minutes=2):
            reject_msg = self.message_lib.Reject()
            try:
                reject_msg.RefSeqNum = msg.Header.MsgSeqNum
                reject_msg.RefMsgType = msg._msgtype
                reject_msg.RefTagID = msg.Header.tags.SendingTime
                reject_msg.Text = "SendingTime accuracy problem"                
                reject_msg.SessionRejectReason = self.message_lib.SessionRejectReason.ENUM_SENDINGTIME_ACCURACY_PROBLEM
            except:
                pass
            self.send_message(reject_msg)
            raise fix_errors.FIXSendTimeAccuracyError("SendingTime accuracy problem")
            

