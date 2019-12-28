import logging
import asyncio
import fix_engine
import heapq

class FIXInvalidMessageError(Exception) : pass
class FIXInvalidFirstMessage(Exception) : pass

logger = logging.getLogger(__name__)

class MessageValidatorMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_callback(None, self.on_first_message, priority = fix_engine.CallbackWrapper.CALLBACK_PRIORITY.FIRST)
        self.register_callback(None, self.on_validate_message)
        

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
            raise FIXInvalidFirstMessage("First message not a logon")
        heapq.heappop(self.call_back_register[None])


    def on_validate_message(self, msg):
        if msg.Header.SenderCompID != self.settings['TargetCompID']:
            raise FIXInvalidMessageError(f"Invalid SenderCompID [{msg.Header.SenderCompID}] on message")
        if msg.Header.TargetCompID != self.settings['SenderCompID']:
            raise FIXInvalidMessageError(f"Invalid TargetCompID [{msg.Header.TargetCompID}] on message")        

    def do_callbacks_in_thread(self):
        try:
            super().do_callbacks_in_thread()
        except FIXInvalidMessageError as e:
            self.application.on_error(e)
            logger.error(e)
            self.logout(e)
            return
        except FIXInvalidFirstMessage as e:
            self.application.on_error(e)
            logger.error(e)
            self.close_connection(False)
            return
