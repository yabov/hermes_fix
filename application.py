import asyncio
import fix_engine

class Application:
    def __init__(self):
        self.engines = {}

    def on_created(self, session_name):
        pass

    def on_engine_initialized(self, engine, session_name):
        self.engines[session_name] = engine

    def on_register_callbacks(self, session_name):
        pass

    def send_message(self, session_name, msg):
        self.engines[session_name].send_message(msg)

    def register_callback(self, session_name, msg_class, callback, priority=fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func = None, one_time = False):
        self.engines[session_name].register_callback(msg_class, callback, priority, check_func, one_time)

    def on_error(self, session_name, error): 
        pass

    def close_connection(self, session_name):
        self.engines[session_name].close_connection()

    def on_connection_closed(self, session_name):
        del self.engines[session_name]