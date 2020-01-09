import asyncio
import logging
import fix_message_library
import datetime
import concurrent.futures
import queue
import heapq
import threading
import functools


from fix_engine_mixins import heartbeat_mixin, sequence_check_mixin, message_validator_mixin
import fix_errors

logger = logging.getLogger(__name__)

B_TABLE = bytes.maketrans(b'\x01', b'|')

ENGINE_LOGON_MAP = {}

class CallBackPriorityExistsError(Exception): pass
class CallbackRegistrar:
    class CALLBACK_PRIORITY:
        FIRST = 0
        HIGH = 100
        NORMAL = 200
        LOW = 300
        LAST = 400
        BEFORE = -1
        AFTER = 1
    def __init__(self, loop):
        self.priority_callback_map = {}
        self.loop = loop

    def add_callback(self, msg_class, callback, priority, check_func = None, one_time= False, timeout= None, timeout_cb = None):
        priority_cb = CallbackWrapper(priority, callback, check_func, self.loop, timeout = timeout, timeout_cb = timeout_cb)
        if one_time:
            priority_cb.clean_up_func = lambda : self.remove_callback(msg_class, priority, callback)
        

        if msg_class is None: #None will be used to register a callback for all messages
            if None not in self.priority_callback_map:
                self.priority_callback_map[None] = [priority_cb]
            else:                    
                self.priority_callback_map[None].append(priority_cb)
        else:
            if msg_class._msgtype not in self.priority_callback_map:
                self.priority_callback_map[msg_class._msgtype] = [priority_cb]
            else:
                self.priority_callback_map[msg_class._msgtype].append(priority_cb)
        

    def get_callbacks(self, msg):
        temp_list = self.priority_callback_map.get(None, []) + self.priority_callback_map.get(msg._msgtype, [])
        temp_list.sort() 
        return temp_list

    def remove_callback(self, msg_class, priority, callback):
        if msg_class is None:
            self.priority_callback_map[None].remove(CallbackWrapper(priority, callback, None))
        else:
            self.priority_callback_map[msg_class._msgtype].remove(CallbackWrapper(priority, callback, None))




class CallbackWrapper:
    def __init__(self, priority, callback, check_func = None, loop = None, clean_up_func = None, timeout = None, timeout_cb = None):
        self.priority = priority
        self.callback = callback
        self.check_func = check_func or (lambda x: True)
        self.clean_up_func = clean_up_func
        self.loop = loop
        self.timer_handle = None
        self.timeout_cb = timeout_cb
        if timeout:
            self.loop.call_soon_threadsafe(self.schedule_timer, timeout)
    
    def schedule_timer(self, timeout):
        self.timer_handle = self.loop.call_later(timeout, self.timeout_cb)

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority and self.callback == other.callback

    def __call__(self, msg):
        if self.check_func(msg) or msg is None:
            if self.timer_handle:
                self.timer_handle.cancel()
            if self.clean_up_func:
                self.clean_up_func()
            return self.callback(msg)

        return None

    def __repr__(self):
        return f"{self.priority},{self.callback}"


class FIXEngineBase():
    def __init__(self, application, store_factory, session_settings, reader, writer, settings = None, max_workers = None):
        self.application = application
        self.store_factory = store_factory
        self.session_settings = session_settings
        self.store = None
        self.time_format = None
        self.application = application
        self.settings = settings
        self.reader = reader
        self.writer = writer

        self.message_lib = None

        self.engine_key = None

        self.msg_seq_num_out = 1

        self.loop = asyncio.get_running_loop()

        self.tid = threading.current_thread()

        self.application.engine = self
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

        self.admin_callback_register = CallbackRegistrar(self.loop)
        self.callback_register = CallbackRegistrar(self.loop)

        self.msg_queue = queue.Queue()

        self.waiting_for_logout = False

    def make_engine_key(self):
        raise NotImplementedError

    def is_logged_on(self):
        return ENGINE_LOGON_MAP.get(self.engine_key, False)

    async def send_logon(self):
        logon_msg = self.build_logon_msg()
        self.send_message(logon_msg)

    def send_reject(self, ref_seq_num, ref_msg_type, ref_tag_id, text, reason):
        reject_msg = self.message_lib.fix_messages.Reject()
        try:
            if ref_seq_num : reject_msg.RefSeqNum = ref_seq_num
            if text : reject_msg.Text = text
            if ref_msg_type : reject_msg.RefMsgType = ref_msg_type
            if ref_tag_id : reject_msg.RefTagID = ref_tag_id
            if reason : reject_msg.SessionRejectReason = reason
        except:
            pass
        self.send_message(reject_msg)

    def send_biz_reject(self, ref_seq_num, ref_msg_type, ref_id, text, reason):
        try: #try to send business reject message, if it fails, fall back on session reject
            reject_msg = self.message_lib.fix_messages.BusinessMessageReject()
            if ref_seq_num : reject_msg.RefSeqNum = ref_seq_num
            if text : reject_msg.Text = text
            if ref_msg_type : reject_msg.RefMsgType = ref_msg_type
            if ref_id : reject_msg.BusinessRejectRefID = ref_id
            if reason : reject_msg.BusinessRejectReason = reason
            self.send_message(reject_msg)
        except:
            self.send_reject( ref_seq_num, ref_msg_type, ref_id, text, reason)

    def on_logon(self, msg):
        raise NotImplementedError

    def init_message_lib(self, begin_string):
        self.message_lib = fix_message_library.MESSAGE_BASE_LIBRARY[begin_string]

    def init_settings(self):
        #TODO generate messages and swap in for generated class

        self.store = self.store_factory.create_storage(self.settings)
        self.time_format = '%Y%m%d-%H:%M:%S' if self.settings.get('ForceSecondsPrecision', None)  == 'True' else '%Y%m%d-%H:%M:%S.%f'

        self.msg_seq_num_out = self.store.get_current_out_seq()
        self.engine_key = self.make_engine_key()
        self.application.on_engine_initialized() #pass in the engine to the application

    def log_out_sleep(self):
        raise fix_errors.FIXHardKillError("Failed to get logout while waiting, closing connection")

    def on_logout(self, msg):
        if self.is_logged_on():
            self.waiting_for_logout = False
            self.logout(None, wait_interval =0, send_test_msg=False)
            self.close_connection()

    def on_logout_response(self, msg):
        self.close_connection()


    def logout(self, text= None, wait_interval = 10, send_test_msg = True):
        if self.waiting_for_logout:
            logger.warning("Already sent logout not sending another")
            return
        if self.is_logged_on():
            if wait_interval:
                self.register_admin_callback(self.message_lib.fix_messages.Logout, self.on_logout_response, 
                        priority= CallbackRegistrar.CALLBACK_PRIORITY.HIGH,
                        one_time=True, timeout=wait_interval, timeout_cb=self.log_out_sleep)

            msg = self.message_lib.fix_messages.Logout()
            if text: msg.Text = text
            self.send_message(msg)
            self.waiting_for_logout = True
        else:
            logger.warning("logout called on logged off session")


    def register_admin_callback(self, msg_class, callback, priority = CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func = None, one_time = False, timeout = None, timeout_cb = None):
        self._register_cb(self.admin_callback_register, msg_class, callback, priority, check_func, one_time, timeout, timeout_cb)

    def register_callback(self, msg_class, callback, priority = CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func = None, one_time = False, timeout = None, timeout_cb = None):
        self._register_cb(self.callback_register, msg_class, callback, priority, check_func, one_time, timeout, timeout_cb)

    def _register_cb(self, cb_register, msg_class, callback, priority, check_func, one_time, timeout, timeout_cb):
        timeout_func_wrapper = lambda : self.pool.submit(self.do_callbacks, None, [lambda x : timeout_cb()])
        cb_register.add_callback(msg_class, callback, priority, check_func, one_time, timeout, timeout_func_wrapper)

    def register_admin_messages(self):
        self.register_admin_callback(self.message_lib.fix_messages.Logout, self.on_logout)

    def find_session(self, header, settings):
        for section in settings.values():
            if section.get('SenderCompID') == header.TargetCompID and section.get('TargetCompID') == header.SenderCompID and section.get('BeginString') == header.BeginString:
                return section
        
        logger.debug(f"Available Sessions {[section for section in settings.values()]}")
        raise fix_errors.FIXSessionNotFound("Session not found")

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
                await self.loop.run_in_executor(self.pool, self.do_callbacks_in_thread)
        finally:
            await self.writer.drain()

    def do_callbacks_in_thread(self):
        msg = self.msg_queue.get()
        admin_callbacks = self.admin_callback_register.get_callbacks(msg)
        callbacks = self.callback_register.get_callbacks(msg)

        if self.do_callbacks(msg, admin_callbacks):
            if len(callbacks) == 0 and msg._msgcat != 'admin':
                error = f"Unsupported Message Type [{msg._msgtype}]"
                logger.error(error)
                self.application.on_error(fix_errors.FIXUnsupportedMessageTypeError(msg.Header.MsgSeqNum, msg._msgtype, None, error, self.message_lib.fields.BusinessRejectReason.ENUM_UNSUPPORTED_MESSAGE_TYPE))
                self.send_biz_reject(msg.Header.MsgSeqNum, msg._msgtype, None, error, self.message_lib.fields.BusinessRejectReason.ENUM_UNSUPPORTED_MESSAGE_TYPE)

            self.do_callbacks(msg, callbacks)

    def do_callbacks(self, msg, callbacks):
        for callback in callbacks:
            response_msg = None
            try:
                response_msg = callback(msg)
            except fix_errors.FIXDropMessageError as e:
                self.application.on_error(e)
                return False
            except fix_errors.FIXRejectAndLogoutError as e:
                self.application.on_error(e)
                self.store.set_current_in_seq(msg.Header.MsgSeqNum)
                self.send_reject(msg.Header.MsgSeqNum, e.RefMsgType, e.RefTagID, e.Text, e.SessionRejectReason)
                self.logout(e.Text, wait_interval=e.wait_interval, send_test_msg = e.send_test_msg)
                return False
            except fix_errors.FIXRejectError as e:
                self.application.on_error(e)
                self.store.set_current_in_seq(msg.Header.MsgSeqNum)
                self.send_reject(msg.Header.MsgSeqNum, e.RefMsgType, e.RefTagID, e.Text, e.SessionRejectReason)
                return False            
            except fix_errors.FIXLogoutError as e:
                self.application.on_error(e)
                logger.error(e)
                self.logout(e.Text, e.wait_interval, e.send_test_msg)
                if not e.wait_interval:
                    self.close_connection(True)
                return False
            except fix_errors.FIXHardKillError as e:
                self.application.on_error(e)
                logger.error(e)
                self.close_connection(False)
                return False
            except:
                logger.exception("Uncaught exception")
            if response_msg is not None:
                self.send_message(response_msg)

        return True

    def close_connection(self, reset_logon = True):
        if reset_logon:
            ENGINE_LOGON_MAP[self.engine_key] = False

    def build_logon_msg(self):
        logon = self.message_lib.fix_messages.Logon()
        logon.EncryptMethod = self.message_lib.fields.EncryptMethod.ENUM_NONE
        return logon

    def send_message(self, msg, resend = False):
        #We want send_message to block but blocking in the loop's thread will deadlock
        if self.tid == threading.current_thread():
            self._send( msg, resend)
        else:
            future = asyncio.run_coroutine_threadsafe(self._send_await(msg, resend), self.loop)
            future.result()

    async def _send_await(self, *args, **kwargs):
        return self._send(*args, **kwargs)

    def _send(self, msg, resend = False):
        if self.waiting_for_logout:
            logger.warning("Logout sent, not sending anymore messages")
            return
        msg.Header.BeginString = msg.Header.BeginString or self.settings['BeginString']
        msg.Header.MsgType = msg._msgtype
        msg.Header.MsgSeqNum = msg.Header.MsgSeqNum  or self.msg_seq_num_out
        msg.Header.SendingTime = msg.Header.SendingTime or datetime.datetime.utcnow().strftime(self.time_format)
        msg.Header.TargetCompID = msg.Header.TargetCompID or self.settings['TargetCompID']
        msg.Header.SenderCompID = msg.Header.SenderCompID or self.settings['SenderCompID']

        buffer =  bytes(msg)
        logger.info(f"Outgoing msg [{buffer.translate(B_TABLE)}]")
        try:
            self.writer.write(buffer)
        except:
            logger.exception(f"Failed to send message [{buffer.translate(B_TABLE)}]")
            return
        
        if not resend:
            self.store.add_message(self.msg_seq_num_out, msg._msgtype, buffer)
            self.msg_seq_num_out +=1
            self.store.set_current_out_seq(self.msg_seq_num_out)

class FIXEngine(message_validator_mixin.MessageValidatorMixin, heartbeat_mixin.HeartBeatMixin, sequence_check_mixin.SequenceCheckerMixin, FIXEngineBase): pass

class FIXEngineInitiator(FIXEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_message_lib(self.settings['BeginString'])
        self.init_settings()
        self.register_admin_messages()

        self.application.on_register_callbacks()

    def make_engine_key(self):
        ip = self.settings.get('SocketConnectHost', 'localhost')
        port = self.settings['SocketConnectPort']
        sender_comp_id = self.settings['SenderCompID']
        target_comp_id = self.settings['TargetCompID']

        return (ip, port, sender_comp_id, target_comp_id)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(self.message_lib.fix_messages.Logon, self.on_logon, priority = CallbackRegistrar.CALLBACK_PRIORITY.HIGH)
        
    def on_logon(self, msg):
        ENGINE_LOGON_MAP[self.engine_key] = True


class FIXEngineAcceptor(FIXEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_admin_callback(None, self.on_first_acceptor_msg, priority=CallbackRegistrar.CALLBACK_PRIORITY.FIRST+CallbackRegistrar.CALLBACK_PRIORITY.BEFORE, 
            one_time=True, timeout=10, timeout_cb = self.on_no_logon)

    def make_engine_key(self):
        ip = self.settings.get('SocketAcceptHost', 'localhost')
        port = self.settings['SocketAcceptPort']
        sender_comp_id = self.settings['SenderCompID']
        target_comp_id = self.settings['TargetCompID']

        return (ip, port, sender_comp_id, target_comp_id)

    def on_no_logon(self):
        raise fix_errors.FIXHardKillError("No Logon received")

    #creating the first callback lets us get the beginstring and set a default message_lib based on version
    def on_first_acceptor_msg(self, msg):
        self.init_message_lib(msg.Header.BeginString)
        self.register_admin_messages()
        self.application.on_register_callbacks()
        self.msg_queue.put(msg)
        self.do_callbacks_in_thread()

    def register_admin_messages(self, *args, **kwargs):
        self.register_admin_callback(self.message_lib.fix_messages.Logon, self.on_logon, 
            priority = CallbackRegistrar.CALLBACK_PRIORITY.FIRST) #High priority to init_settings before other checks
        super().register_admin_messages(*args, **kwargs)


    def on_logon(self, msg):
        self.settings = self.find_session(msg.Header, self.session_settings)
        self.init_settings()

        if self.is_logged_on():
            raise fix_errors.FIXSessionExistsError("Session is already logged on")

        ENGINE_LOGON_MAP[self.engine_key] = True
        
        logon_msg = self.build_logon_msg()

        return logon_msg

