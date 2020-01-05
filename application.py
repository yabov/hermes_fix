import asyncio
import fix_engine

class Application:
    def __init__(self):
        self.engine = None

    def on_engine_initialized(self):
        pass

    def on_register_callbacks(self):
        pass

    def on_logon(self):
        pass

    def on_logoff(self):
        pass

    def send_message(self, msg):
        self.engine.send_message(msg)

    def register_callback(self, msg_class, callback, priority=fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func = None, one_time = False):
        self.engine.register_callback(msg_class, callback, priority, check_func, one_time)

    def on_error(self, error): 
        pass

    def close_connection(self):
        self.engine.close_connection()