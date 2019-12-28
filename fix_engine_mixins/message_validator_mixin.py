import logging
import asyncio
import fix_engine
import heapq
import fix_errors

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
        except ConnectionError:
            logger.debug("Connection closed")
            self.close_connection()
            return None
        except asyncio.streams.IncompleteReadError:
            logger.debug("Incomplete read")
            self.close_connection()
            return None
        except Exception as e:
            logger.exception("FAIL")
            self.application.on_error(e)
            logger.error(f"Skipping message because failed to parse message: {e}")
            return None

    def on_first_message(self, msg):
        if not isinstance(msg, self.message_lib.Logon):
            raise fix_errors.FIXInvalidFirstMessage("First message not a logon")
        heapq.heappop(self.call_back_register[None])


    def on_validate_message(self, msg):
        if msg.Header.SenderCompID != self.__TargetCompID:
            raise fix_errors.FIXInvalidMessageError(f"Invalid SenderCompID [{msg.Header.SenderCompID}] on message, expecting [{self.__TargetCompID}]")
        if msg.Header.TargetCompID != self.__SenderCompID:
            raise fix_errors.FIXInvalidMessageError(f"Invalid TargetCompID [{msg.Header.TargetCompID}] on message, expecting [{self.__SenderCompID}]")   
        if msg.Header.BeginString != self.__BeginString:
            raise fix_errors.FIXInvalidMessageError(f"Invalid BeginString [{msg.Header.BeginString}] on message, expecting [{self.__BeginString}]")   

