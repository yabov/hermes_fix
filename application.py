import asyncio
import queue
import logging

from . import fix_engine


logger = logging.getLogger(__name__)

class Application:
    """
    Main application class for interacting with the FIX engine.
    Application should be subclassed and the following functions can be overridden:

    on_created(self, session_name)
    on_engine_initialized(self, session_name, engine)
    on_register_callbacks(self, session_name)
    on_error(self, session_name, error)
    on_reconnect(self, session_name)
    on_connection_closed(self, session_name)

    """

    def __init__(self):
        self.engines = {}
        self.message_queue_map = {}

    def _on_created(self, session_name):
        if session_name not in self.message_queue_map:
            self.message_queue_map[session_name] = queue.Queue()
        self.on_created(session_name)

    def _on_engine_initialized(self, session_name, engine):
        self.engines[session_name] = engine
        self.on_engine_initialized(session_name, engine)
        
    def _on_register_callbacks(self, session_name):
        self.register_callback(session_name, 
                               self.engines[session_name].message_lib.fix_messages.Logon, 
                               self._on_logon, 
                               priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.FIRST)
        self.on_register_callbacks(session_name)

    def _on_logon(self, session_name, msg):
        self.message_queue_map[session_name].put(None) #chaser to ensure that we stop instead of cycling through the queue if send_message fails here
        msg = self.message_queue_map[session_name].get_nowait()
        while msg:
            msg.Header = self.engines[session_name].message_lib.fix_messages.Header()
            msg.Trailer = self.engines[session_name].message_lib.fix_messages.Trailer()
            self.send_message(session_name, msg)
            msg = self.message_queue_map[session_name].get_nowait()

    def send_message(self, session_name, msg):
        """
        Send a FIX message

        session_name is the section name of the config.ini
        msg must be an instance of fix_message.MessageBase

        If send_message errors out or is called while the connection is not available, 
        the message will be queued for the next time the connection is established.

        """
        try:
            self.engines[session_name].send_message(msg)
        except:
            logger.debug("Failed to send message, queuing for next logon")
            self.message_queue_map[session_name].put(msg)

    def register_callback(self, session_name, msg_class, callback, 
                        priority=fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.NORMAL, check_func = None, one_time = False,
                        timeout=None, timeout_cb=None):

        """
        function to register a call back when a message comes to the FIX engine
        the same message can have multiple callbacks registered, use priority to define the order in which they are called

        session_name is the section name of the config.ini

        msg_class is the type of the message for the callback or None for all messages

        callback is the function to be called - must be of signature: func(session_name, msg) -> msg or None
            the return value from the function should be None or of instance MessageBase to be sent as a response

        priority is the callback priority to define in which order callbacks for the same message are called

        check_func is a function of signature: func(msg) -> bool which if returns False will not trigger the callback
            useful when waiting for a specific Ack message with a reference ID in it

        one_time boolean if true de-registers the callback after the first time it is invoked

        timeout in seconds to wait for a callback to be fired
            useful when waiting for a specific Ack

        timeout_cb function of signature func() -> None called if a timeout has occured

        """
        self.engines[session_name].register_callback(msg_class, callback, priority, check_func, one_time)

    def _on_error(self, session_name, error): 
        self.on_error(session_name, error)

    def _on_reconnect(self, session_name):
        self.on_reconnect(session_name)

    def close_connection(self, session_name):
        """
        closes the FIX connection associated with session_name.
        Warning: unless the server is stopped a client will initiate a reconnect
        """
        if session_name in self.engines:
            self.engines[session_name].close_connection()

    def _on_connection_closed(self, session_name):
        self.on_connection_closed(session_name)

    def logout(self, session_name):
        """
        Send a FIX logout
        """
        self.engines[session_name].logout()

    def on_created(self, session_name):
        """
        Called when the application's underlying engine is first created, before a connection is established
        """
        pass

    def on_engine_initialized(self, session_name, engine):
        """
        Called once the engine is initialized.
        For Initiator: called immediately before sending a Logon message
        For Acceptor:  called after reciept of first Logon message from Initiator
        """
        pass
    
    def on_register_callbacks(self, session_name):
        """
        Called to instruct the application to register callbacks 
        """
        pass

    def on_error(self, session_name, error): 
        """
        Called when the FIX engine throws any kind of FIX error as defined in the fix_errors module
        """
        pass

    def on_reconnect(self, session_name):
        """
        Called when a Initiator drops the FIX connection and reconnects
        """
        pass

    def on_connection_closed(self, session_name):
        """
        Called after the FIX connection is closed to perform cleanup.
        Warning: Initiator may attempt to reconnect if server is not stopped
        """
        pass
