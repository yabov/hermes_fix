import asyncio
import concurrent.futures
import datetime
import logging
import queue
import threading

from . import fix_errors, fix_message_library
from .fix_callbacks import CallbackRegistrar
from .fix_engine_mixins import (heartbeat_mixin, message_validator_mixin,
                                sequence_check_mixin, session_manager_mixin)
from .utils.constants import B_TABLE
from .utils.log import logger

ENGINE_LOGON_MAP = {}


class FIXEngineBase():
    def __init__(self, application, store_factory, session_settings, session_name, max_workers=None):
        self.store_factory = store_factory
        self.session_settings = session_settings
        self.store = None
        self.time_format = None
        self.application = application

        self.session_name = session_name
        self.settings = session_settings[session_name]
        self.reader = None  # set by sesion_manager_mixin
        self.writer = None  # set by sesion_manager_mixin

        self.message_lib = None

        self.engine_key = None

        self.msg_seq_num_out = 1

        self.loop = asyncio.get_running_loop()

        self.tid = threading.current_thread()

        self.pool = concurrent.futures.ThreadPoolExecutor(
            max_workers=max_workers)

        self.admin_callback_register = CallbackRegistrar(self.loop)
        self.callback_register = CallbackRegistrar(self.loop)

        self.msg_queue = queue.Queue()

        self.waiting_for_logout = False

    def make_engine_key(self):
        raise NotImplementedError

    def is_logged_on(self):
        return ENGINE_LOGON_MAP.get(self.engine_key, False)

    def send_logon(self):
        logon_msg = self.build_logon_msg()
        self.send_message(logon_msg)

    def send_reject(self, ref_seq_num, ref_msg_type, ref_tag_id, text, reason):
        reject_msg = self.message_lib.fix_messages.Reject()
        try:
            if ref_seq_num:
                reject_msg.RefSeqNum = ref_seq_num
            if text:
                reject_msg.Text = text
            if ref_msg_type:
                reject_msg.RefMsgType = ref_msg_type
            if ref_tag_id:
                reject_msg.RefTagID = ref_tag_id
            if reason:
                reject_msg.SessionRejectReason = reason
        except:
            pass
        self.send_message(reject_msg)

    def send_biz_reject(self, ref_seq_num, ref_msg_type, ref_id, text, reason):
        try:  # try to send business reject message, if it fails, fall back on session reject
            reject_msg = self.message_lib.fix_messages.BusinessMessageReject()
            if ref_seq_num:
                reject_msg.RefSeqNum = ref_seq_num
            if text:
                reject_msg.Text = text
            if ref_msg_type:
                reject_msg.RefMsgType = ref_msg_type
            if ref_id:
                reject_msg.BusinessRejectRefID = ref_id
            if reason:
                reject_msg.BusinessRejectReason = reason
            self.send_message(reject_msg)
        except:
            self.send_reject(ref_seq_num, ref_msg_type, ref_id, text, reason)

    def on_logon(self, session_name, msg):
        raise NotImplementedError

    def init_message_lib(self, begin_string):
        self.message_lib = fix_message_library.MESSAGE_BASE_LIBRARY[begin_string]

    def init_settings(self):
        self.store = self.store_factory.create_storage(self.settings)
        self.time_format = self.settings.get(
            'TimeFormat', fallback='%Y%m%d-%H:%M:%S.%f')
        self.msg_seq_num_out = self.store.get_current_out_seq()
        self.engine_key = self.make_engine_key()

        data_dict = self.settings.get('DataDictionary', None)
        if data_dict:
            self.message_lib = fix_message_library.load_data_dict(data_dict, self.engine_key)

        # pass in the engine to the application
        self.application._on_engine_initialized(self.session_name, self)

    def log_out_sleep(self):
        raise fix_errors.FIXHardKillError(
            "Failed to get logout while waiting, closing connection")

    def on_logout(self, session_name, msg):
        if self.is_logged_on():
            self.waiting_for_logout = False
            self.logout(None, wait_interval=0, send_test_msg=False)
            self.close_connection()

    def on_logout_response(self, session_name, msg):
        self.waiting_for_logout = False
        self.close_connection()

    def logout(self, text=None, wait_interval=10, send_test_msg=True):
        if self.waiting_for_logout:
            logger.warning("Already sent logout not sending another")
            return
        if self.is_logged_on():
            if wait_interval:
                self.register_admin_callback(self.message_lib.fix_messages.Logout, self.on_logout_response,
                                             priority=CallbackRegistrar.CALLBACK_PRIORITY.HIGH,
                                             one_time=True, timeout=wait_interval, timeout_cb=self.log_out_sleep)

            msg = self.message_lib.fix_messages.Logout()
            if text:
                msg.Text = text
            self.send_message(msg)
            self.waiting_for_logout = True
        else:
            logger.warning("logout called on logged off session")

    def register_admin_callback(self, msg_class, callback, priority=CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func=None, one_time=False, timeout=None, timeout_cb=None):
        self._register_cb(self.admin_callback_register, msg_class,
                          callback, priority, check_func, one_time, timeout, timeout_cb)

    def register_callback(self, msg_class, callback, priority=CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func=None, one_time=False, timeout=None, timeout_cb=None):
        self._register_cb(self.callback_register, msg_class, callback,
                          priority, check_func, one_time, timeout, timeout_cb)

    def _register_cb(self, cb_register, msg_class, callback, priority, check_func, one_time, timeout, timeout_cb):
        def timeout_func_wrapper(): return self.pool.submit(
            self.do_callbacks, None, [lambda session_msg, msg: timeout_cb()])
        cb_register.add_callback(
            msg_class, callback, priority, check_func, one_time, timeout, timeout_func_wrapper)

    def register_admin_messages(self):
        self.register_admin_callback(
            self.message_lib.fix_messages.Logout, self.on_logout)

    def find_session(self, header, settings):
        for name, section in settings.items():
            if section.get('SenderCompID') == header.TargetCompID and section.get('TargetCompID') == header.SenderCompID and section.get('BeginString') == header.BeginString:
                return name, section

        logger.debug(
            f"Available Sessions {[section for section in settings.values()]}")
        raise fix_errors.FIXSessionNotFound("Session not found")

    async def parse_message(self):
        msg, buffer, missed_fields = await fix_message_library.create_message_from_stream(self.reader, self.message_lib, self.settings)
        logger.info(f'Incoming msg [{buffer.translate(B_TABLE)}]')

        return msg, buffer, missed_fields

    async def serve_client(self):
        await self.loop_run()  # first loop for logon message
        while self.is_logged_on():
            await self.loop_run()
        logger.debug("Ending Server Loop")

    async def loop_run(self):
        msg, _, _ = await self.parse_message()
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
                self.application._on_error(self.session_name,
                                           fix_errors.FIXUnsupportedMessageTypeError(msg.Header.MsgSeqNum, msg._msgtype,
                                                                                     None, error, self.message_lib.fields.BusinessRejectReason.ENUM_UNSUPPORTED_MESSAGE_TYPE))
                self.send_biz_reject(msg.Header.MsgSeqNum, msg._msgtype, None, error,
                                     self.message_lib.fields.BusinessRejectReason.ENUM_UNSUPPORTED_MESSAGE_TYPE)

            self.do_callbacks(msg, callbacks)

    def do_callbacks(self, msg, callbacks):
        for callback in callbacks:
            response_msg = None
            try:
                response_msg = callback(self.session_name, msg)
            except fix_errors.FIXDropMessageError as e:
                self.application._on_error(self.session_name, e)
                return False
            except fix_errors.FIXRejectAndLogoutError as e:
                self.application._on_error(self.session_name, e)
                self.store.set_current_in_seq(msg.Header.MsgSeqNum)
                self.send_reject(msg.Header.MsgSeqNum, e.RefMsgType,
                                 e.RefTagID, e.Text, e.SessionRejectReason)
                self.logout(e.Text, wait_interval=e.wait_interval,
                            send_test_msg=e.send_test_msg)
                return False
            except fix_errors.FIXRejectError as e:
                self.application._on_error(self.session_name, e)
                logger.error(e)
                self.store.set_current_in_seq(msg.Header.MsgSeqNum)
                self.send_reject(msg.Header.MsgSeqNum, e.RefMsgType,
                                 e.RefTagID, e.Text, e.SessionRejectReason)
                return False
            except fix_errors.FIXLogoutError as e:
                self.application._on_error(self.session_name, e)
                logger.error(e)
                self.logout(e.Text, e.wait_interval, e.send_test_msg)
                if not e.wait_interval:
                    self.close_connection(True)
                return False
            except fix_errors.FIXHardKillError as e:
                self.application._on_error(self.session_name, e)
                logger.error(e)
                self.close_connection(False)
                return False
            except:
                if self.is_logged_on():
                    logger.exception("Uncaught exception")
            if response_msg is not None:
                self.send_message(response_msg)

        return True

    def close_connection(self, reset_logon=True):
        if reset_logon:
            self.waiting_for_logout = False
            ENGINE_LOGON_MAP[self.engine_key] = False
        if self.store:
            self.store.close()

        self.application._on_connection_closed(self.session_name)

    def build_logon_msg(self):
        logon = self.message_lib.fix_messages.Logon()
        logon.EncryptMethod = self.message_lib.fields.EncryptMethod.ENUM_NONE
        return logon

    def send_message(self, msg, resend=False):
        # We want send_message to block but blocking in the loop's thread will deadlock
        if self.tid == threading.current_thread():
            self._send(msg, resend)
        else:
            future = asyncio.run_coroutine_threadsafe(
                self._send_await(msg, resend), self.loop)
            future.result()

    async def _send_await(self, *args, **kwargs):
        self._send(*args, **kwargs)
        await self.writer.drain()

    def _send(self, msg, resend=False):
        if self.waiting_for_logout:
            logger.warning("Logout sent, not sending anymore messages")
            return
        msg.Header.BeginString = msg.Header.BeginString or self.settings['BeginString']
        msg.Header.MsgType = msg._msgtype
        msg.Header.MsgSeqNum = msg.Header.MsgSeqNum or self.msg_seq_num_out
        msg.Header.SendingTime = msg.Header.SendingTime or datetime.datetime.utcnow(
        ).strftime(self.time_format)
        msg.Header.TargetCompID = msg.Header.TargetCompID or self.settings['TargetCompID']
        msg.Header.SenderCompID = msg.Header.SenderCompID or self.settings['SenderCompID']

        buffer = bytes(msg)
        logger.info(f"Outgoing msg [{buffer.translate(B_TABLE)}]")
        try:
            self.writer.write(buffer)
        except:
            logger.exception(
                f"Failed to send message [{buffer.translate(B_TABLE)}]")
            raise

        try:
            if not resend:  # it's possible that is self.store.clean_up is called while sending a message we'd fail to add it but at that point it doesn't matter
                self.store.add_message(
                    self.msg_seq_num_out, msg._msgtype, buffer)
                self.msg_seq_num_out += 1
                self.store.set_current_out_seq(self.msg_seq_num_out)
        except:
            if self.store.db:
                raise


class FIXEngine(message_validator_mixin.MessageValidatorMixin,
                heartbeat_mixin.HeartBeatMixin,
                sequence_check_mixin.SequenceCheckerMixin,
                FIXEngineBase):
    pass


class FIXEngineInitiator(session_manager_mixin.SessionManagerInitiatorMixin, FIXEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_message_lib(self.settings['BeginString'])
        self.init_settings()
        self.register_admin_messages()

        self.application._on_register_callbacks(self.session_name)

    def make_engine_key(self):
        ip = self.settings.get('SocketConnectHost', 'localhost')
        port = self.settings['SocketConnectPort']
        sender_comp_id = self.settings['SenderCompID']
        target_comp_id = self.settings['TargetCompID']

        return (ip, port, sender_comp_id, target_comp_id)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(self.message_lib.fix_messages.Logon,
                                     self.on_logon, priority=CallbackRegistrar.CALLBACK_PRIORITY.HIGH)

    def on_logon(self, session_name, msg):
        ENGINE_LOGON_MAP[self.engine_key] = True


class FIXEngineAcceptor(session_manager_mixin.SessionManagerAcceptorMixin, FIXEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_message_timeout = self.session_settings['DEFAULT'].get(
            "FirstMessageTimeout", fallback=10)
        self.register_admin_callback(None, self.on_first_acceptor_msg,
                                     priority=CallbackRegistrar.CALLBACK_PRIORITY.FIRST +
                                     CallbackRegistrar.CALLBACK_PRIORITY.BEFORE,
                                     one_time=True, timeout=first_message_timeout, timeout_cb=self.on_no_logon)

    def make_engine_key(self):
        ip = self.settings.get('SocketAcceptHost', 'localhost')
        port = self.settings['SocketAcceptPort']
        sender_comp_id = self.settings['SenderCompID']
        target_comp_id = self.settings['TargetCompID']

        return (ip, port, sender_comp_id, target_comp_id)

    def on_no_logon(self):
        raise fix_errors.FIXHardKillError("No Logon received")

    # creating the first callback lets us get the beginstring and set a default message_lib based on version
    def on_first_acceptor_msg(self, session_name, msg):
        self.init_message_lib(msg.Header.BeginString)

        # TODO: move to on_logon. currently here because application's callbacks need to be registered before logon which needs session_name and the engine
        self.session_name, self.settings = self.find_session(
            msg.Header, self.session_settings)

        self.init_settings()

        self.register_admin_messages()
        self.application._on_register_callbacks(self.session_name)

        self.msg_queue.put(msg)
        self.do_callbacks_in_thread()

    def register_admin_messages(self, *args, **kwargs):
        self.register_admin_callback(self.message_lib.fix_messages.Logon, self.on_logon,
                                     priority=CallbackRegistrar.CALLBACK_PRIORITY.HIGH + CallbackRegistrar.CALLBACK_PRIORITY.BEFORE)
        super().register_admin_messages(*args, **kwargs)

    def on_logon(self, session_name, msg):
        if self.is_logged_on():
            raise fix_errors.FIXSessionExistsError(
                "Session is already logged on")

        ENGINE_LOGON_MAP[self.engine_key] = True

        logon_msg = self.build_logon_msg()
        return logon_msg
