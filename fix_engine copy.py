import asyncio
import logging
import fix_message_library
import datetime
import concurrent.futures
import queue
import heapq

from fix_engine_mixins import heartbeat_mixin, sequence_check_mixin, message_validator_mixin

logger = logging.getLogger(__name__)

B_TABLE = bytes.maketrans(b'\x01', b'|')

ENGINE_LOGON_MAP = {}

class FIXEngineError(Exception): pass
class FIXSessionExistsError(Exception): pass
class FIXSessionNotFound(Exception):pass
class FIXGarbledMessageError(Exception) : pass

class CallbackWrapper:
    class CALLBACK_PRIORITY:
        FIRST = 0
        HIGH = 10
        NORMAL = 20
        LOW = 30
        LAST = 40
    def __init__(self, priority, callback):
        self.priority = priority
        self.callback = callback

    def __lt__(self, other):
        return self.priority < other.priority

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs)

    def __repr__(self):
        return f"{self.priority},{self.callback}"


class FIXEngineBase():
    def __init__(self, application, store_factory, session_settings, reader, writer, settings = None, max_workers = None):
        self.application = application
        self.store_factory = store_factory
        self.session_settings = session_settings
        self.store = None
        self.application = application
        self.settings = settings
        self.reader = reader
        self.writer = writer

        #I don't like setting the message_lib to a default but without it I cannot register admin messages callback cleanly
        self.message_lib = fix_message_library.MESSAGE_LIBRARY['FIX.4.2'] 

        self.engine_key = None

        self.logout_waiter = None

        self.call_back_register = {}
        self.in_loop_callback_register = {}

        self.msg_seq_num_out = 1

        self.loop = asyncio.get_running_loop()

        self.register_admin_messages()
        self.application.engine = self
        self.application.on_register_callbacks()
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self.msg_queue = queue.Queue()

    def make_engine_key(self):
        raise NotImplementedError

    def is_logged_on(self):
        return ENGINE_LOGON_MAP.get(self.engine_key, False)

    async def send_logon(self):
        logon_msg = self.build_logon_msg()
        self.send_message(logon_msg)

    def on_logon(self, msg):
        raise NotImplementedError

    def init_settings(self):
        self.message_lib = fix_message_library.MESSAGE_LIBRARY[self.settings['BeginString']]

        #TODO generate messages and swap in for generated class

        self.store = self.store_factory.create_storage(self.settings)

        self.msg_seq_num_out = self.store.get_current_out_seq()
        self.engine_key = self.make_engine_key()
        self.application.on_engine_initialized() #pass in the engine to the application

    def log_out_sleep(self):
        self.on_logout(None)

    def on_logout(self, msg):
        if self.logout_waiter:
            self.logout_waiter.cancel()
        if self.is_logged_on():
            self.logout()
            self.close_connection()

    def logout(self, text= None):
        logger.debug(f"Logging out {self.is_logged_on()}")
        if self.is_logged_on():
            msg = self.message_lib.Logout()
            msg.Text = text
            self.send_message(msg)
            self.logout_waiter = self.loop.call_later(30, self.log_out_sleep)
                
    def register_callback(self, msg_class, callback, priority = CallbackWrapper.CALLBACK_PRIORITY.NORMAL):
        priority_cb = [CallbackWrapper(priority, callback)]
        if msg_class is None: #None will be used to register a callback for all messages
            if None not in self.call_back_register:
                heapq.heapify(priority_cb)
                self.call_back_register[None] = priority_cb
            else:
                heapq.heappush(self.call_back_register[None], priority_cb[0])
        else:
            if msg_class._msgtype not in self.call_back_register:
                heapq.heapify([priority_cb])
                self.call_back_register[msg_class._msgtype] = priority_cb
            else:
                heapq.heappush(self.call_back_register[msg_class._msgtype], priority_cb[0])

    def register_admin_messages(self):
        #self.register_callback(None, self.on_first_message)
        self.register_callback(self.message_lib.Logout, self.on_logout)

    def find_session(self, header, settings):
        for section in settings.values():
            if section.get('SenderCompID') == header.TargetCompID and section.get('TargetCompID') == header.SenderCompID and section.get('BeginString') == header.BeginString:
                return section
        
        logger.debug(f"Available Sessions {[section for section in settings.values()]}")
        raise FIXSessionNotFound("Session not found")

    async def parse_message(self):
        msg, buffer = await fix_message_library.create_message_from_stream(self.reader, self.message_lib)
        logger.info(f'Incoming msg [{buffer.translate(B_TABLE)}]')

        return msg

    async def serve_client(self):
        await self.loop_run() #first loop for logon message
        while self.is_logged_on():
            await self.loop_run()
        logger.debug("Ending Server Loop")

    async def loop_run(self):
        msg = await self.parse_message()
        try:
            if msg is not None: 
                self.msg_queue.put(msg)
                await self.loop.run_in_executor(None, self.do_callbacks_in_thread)
        finally:
            await self.writer.drain()

    def do_callbacks_in_thread(self):
        msg = self.msg_queue.get()
        callbacks = list(heapq.merge(self.call_back_register.get(None, []), self.call_back_register.get(msg._msgtype, [])))
        #callbacks = self.call_back_register.get(None, []) + self.call_back_register.get(msg._msgtype, [])
        if not callbacks:
            logger.warning(f"Received unregistered message type {msg._msgtype}")
            return

        for callback in callbacks:
            #logger.debug(callback)
            response_msg = None
            try:
                response_msg = callback(msg)
            except (FIXEngineError, FIXSessionNotFound)  as e:
                if not self.application.on_error(e):
                    logger.error(e)
                    self.close_connection()
                    return
            except (FIXSessionExistsError) as e:
                if not self.application.on_error(e):
                    logger.error(e)
                    self.close_connection(False)
                    raise
            if response_msg is not None:
                self.send_message(response_msg)

    def close_connection(self, reset_logon = True):
        if self.logout_waiter:
            self.logout_waiter.cancel()
        logger.debug(f"Reset logon {reset_logon}")
        if reset_logon:
            ENGINE_LOGON_MAP[self.engine_key] = False

    def build_logon_msg(self):
        logon = self.message_lib.Logon()
        logon.EncryptMethod = self.message_lib.EncryptMethod.ENUM_NONE
        return logon

    def send_message(self, msg, resend_seq_num = None):
        asyncio.run_coroutine_threadsafe(self._send( msg, resend_seq_num), self.loop)

    async def _send(self, msg, resend_seq_num = None):
        msg.Header.BeginString = self.settings['BeginString']
        msg.Header.MsgType = msg._msgtype
        msg.Header.MsgSeqNum = resend_seq_num or self.msg_seq_num_out
        msg.Header.SendingTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        msg.Header.TargetCompID = self.settings['TargetCompID']
        msg.Header.SenderCompID = self.settings['SenderCompID']

        buffer =  bytes(msg)
        logger.info(f"Outgoing msg [{buffer.translate(B_TABLE)}]")
        try:
            self.writer.write(buffer)
        except:
            logger.exception(f"Failed to send message [{buffer.translate(B_TABLE)}]")
            return
        
        if not resend_seq_num:
            self.store.add_message(self.msg_seq_num_out, msg._msgtype, buffer)
            self.msg_seq_num_out +=1
            self.store.set_current_out_seq(self.msg_seq_num_out)


class FIXEngine(message_validator_mixin.MessageValidatorMixin, heartbeat_mixin.HeartBeatMixin, sequence_check_mixin.SequenceCheckerMixin, FIXEngineBase): pass

class FIXEngineInitiator(FIXEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_settings()

    def make_engine_key(self):
        ip = self.settings.get('SocketConnectHost', 'localhost')
        port = self.settings['SocketConnectPort']
        sender_comp_id = self.settings['SenderCompID']
        target_comp_id = self.settings['TargetCompID']

        return (ip, port, sender_comp_id, target_comp_id)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_callback(self.message_lib.Logon, self.on_logon)
        
    def on_logon(self, msg):
        ENGINE_LOGON_MAP[self.engine_key] = True


class FIXEngineAcceptor(FIXEngine):
    def make_engine_key(self):
        ip = self.settings.get('SocketAcceptHost', 'localhost')
        port = self.settings['SocketAcceptPort']
        sender_comp_id = self.settings['SenderCompID']
        target_comp_id = self.settings['TargetCompID']

        return (ip, port, sender_comp_id, target_comp_id)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_callback(self.message_lib.Logon, self.on_logon, priority = CallbackWrapper.CALLBACK_PRIORITY.HIGH) #High priority to init_settings before other checks
        
    def on_logon(self, msg):
        self.settings = self.find_session(msg.Header, self.session_settings)
        self.init_settings()
        if self.is_logged_on():
            raise FIXSessionExistsError("Session is already logged on")

        ENGINE_LOGON_MAP[self.engine_key] = True
        
        logon_msg = self.build_logon_msg()

        return logon_msg

    """
    def on_first_message(self, msg):
        if not isinstance(msg, self.message_lib.Logon):
            raise FIXInvalidFirstMessage("First message not a logon")
        self.settings = self.find_session(msg.Header, self.session_settings)
        self.init_settings()
        self.call_back_register[None].pop(0)
        return self.on_logon(msg)
        """
