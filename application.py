import asyncio
import fix_engine
import queue
import logging

logger = logging.getLogger(__name__)

class Application:
    def __init__(self):
        self.engines = {}
        self.message_queue_map = {}

    def on_created(self, session_name):
        if session_name not in self.message_queue_map:
            self.message_queue_map[session_name] = queue.Queue()

    def on_engine_initialized(self, engine, session_name):
        self.engines[session_name] = engine
        
    def on_register_callbacks(self, session_name):
        self.register_callback(session_name, self.engines[session_name].message_lib.fix_messages.Logon, self.on_logon, 
            priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.FIRST)

    def on_logon(self, session_name, msg):
        self.message_queue_map[session_name].put(None) #chaser to ensure that we stop instead of cycling through the queue if send_message fails here
        msg = self.message_queue_map[session_name].get_nowait()
        while msg:
            msg.Header = self.engines[session_name].message_lib.fix_messages.Header()
            msg.Trailer = self.engines[session_name].message_lib.fix_messages.Trailer()
            self.send_message(session_name, msg)
            msg = self.message_queue_map[session_name].get_nowait()

    def send_message(self, session_name, msg):
        try:
            self.engines[session_name].send_message(msg)
        except:
            logger.debug("Failed to send message, queuing for next logon")
            self.message_queue_map[session_name].put(msg)

    def register_callback(self, session_name, msg_class, callback, priority=fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func = None, one_time = False):
        self.engines[session_name].register_callback(msg_class, callback, priority, check_func, one_time)

    def on_error(self, session_name, error): 
        pass

    def on_reconnect(self, session_name):
        pass

    def close_connection(self, session_name):
        if session_name in self.engines:
            self.engines[session_name].close_connection()

    def on_connection_closed(self, session_name):
        pass
        #del self.engines[session_name]

    def logout(self, session_name):
        self.engines[session_name].logout()