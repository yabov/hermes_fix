import unittest 

import logging
import queue
from datetime import datetime, timedelta

from hermes_fix import fix_errors
from hermes_fix import fix
from hermes_fix import fix_engine
from hermes_fix.message_lib.FIX_4_2 import fix_messages as fix_messages_4_2_0_base
from hermes_fix.fix_callbacks import CallbackRegistrar


logging.basicConfig(level=logging.DEBUG, format= '%(levelname)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

SERVER_QUEUE = queue.Queue()
CLIENT_QUEUE = queue.Queue()

class FIXTestAppServer(fix.Application):
    def on_register_callbacks(self, session_name):
        self.register_callback(session_name, None, self.on_queue_msg)

    def on_queue_msg(self, session_name, msg):
        SERVER_QUEUE.put(msg)

    def on_error(self, session_name, error):
        SERVER_QUEUE.put(error)

class FIXTestAppClient(fix.Application):
    def on_register_callbacks(self, session_name):
        self.register_callback(session_name, None, self.on_queue_msg)

    def on_queue_msg(self, session_name, msg):
        CLIENT_QUEUE.put(msg)    

    def on_error(self, session_name, error):
        CLIENT_QUEUE.put(error)    


class Test(unittest.TestCase):
    def setUp(self):
        #print("Entering", self._testMethodName)
        self.store = fix.FileStoreFactory()
        self.settings = fix.SessionSettings([])
        self.settings.read_dict({self._testMethodName : {'ConnectionType' : 'acceptor',
                    'BeginString' : 'FIX.4.2',
                    'SenderCompID' : 'HOST',
                    'TargetCompID' : self._testMethodName,#'CLIENT',
                    'SocketAcceptPort' : '5001',
                    'FileStorePath' : 'store',
                    'DataDictionary' : '../spec/FIX42.xml',
                    'ConnectionStartTime' : datetime.utcnow().time().strftime('%H:%M:%S'),
                    'ConnectionEndTime' : (datetime.utcnow() + timedelta(seconds = 10)).time().strftime('%H:%M:%S'),
                    'LogonTime': (datetime.utcnow() - timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                    'LogoutTime' : (datetime.utcnow() + timedelta(seconds = 10)).time().strftime('%H:%M:%S')}})

        self.settings_client  = fix.SessionSettings([])
        self.settings_client.read_dict({self._testMethodName : {'ConnectionType' : 'initiator',
            'BeginString' : 'FIX.4.2',
            'SenderCompID' : self._testMethodName,#'CLIENT',
            'TargetCompID' : 'HOST',
            'SocketConnectPort' : '5001',
            'SocketConnectHost' : 'localhost',
            'FileStorePath' : 'store',
            'DataDictionary' : '../spec/FIX42.xml',
            'ConnectionStartTime' : datetime.utcnow().time().strftime('%H:%M:%S'),
            'ConnectionEndTime' : (datetime.utcnow() + timedelta(seconds = 10)).time().strftime('%H:%M:%S'),
            'LogonTime': (datetime.utcnow() - timedelta(seconds=10)).time().strftime('%H:%M:%S'),
            'LogoutTime' : (datetime.utcnow() + timedelta(seconds = 10)).time().strftime('%H:%M:%S')}})


        self.client_app = FIXTestAppClient()
        self.client = fix.SocketConnection(self.client_app, self.store, self.settings_client)
        self.server_app = FIXTestAppServer()
        self.server = fix.SocketConnection(self.server_app, self.store, self.settings)

    def do_logout(self, client_app):
        client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)

    """	Receive Logon<A> message"""
    """Respond with Logon<A> response message"""
    def test_valid_logon(self):

        self.server.start()
        self.client.start()

        resp_logon = SERVER_QUEUE.get(timeout=2)
        sent_logon = CLIENT_QUEUE.get(timeout=2)

        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)

        self.do_logout(self.client_app)


    """If MsgSeqNum(34) is too high then send ResendRequest<2>"""
    def test_valid_logon_seq_high(self):

        def register_hack(session_name):
            self.server_app.register_callback(session_name, None, self.server_app.on_queue_msg)
            self.server_app.engines[session_name].msg_seq_num_out = 10



        self.server_app.on_register_callbacks = register_hack
        self.server.start()
        self.client.start()
                

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(self.client_app)

    """Invalid Logon<A> message
        Generate an "error" condition in test output
        (Optional) Send Reject<3> message with RefSeqNum(45) referencing Logon<A> message’s MsgSeqNum and with Text(58) referencing error condition
        Send Logout<5> message with Text(58) referencing error condition
        Disconnect
        """
    def atest_invalid_logon(self):
        pass
        #need to implement passwords and other checks

    """First message received is not a Logon<A> message.	
        Log an error “first message not a logon”
        Disconnect
    """
    def test_invalid_first_message(self):
        hb = fix_messages_4_2_0_base.Heartbeat()
        hb.Header.BeginString = 'FIX.4.2'
        hb.Header.SenderCompID = 'CLIENT'
        hb.Header.TargetCompID = 'HOST'
        hb.Header.MsgSeqNum = 1
        
        def on_logon_hack(session_name, msg):
            #self.server_app.engines[self._testMethodName].settings = self.server_app.engines[self._testMethodName].find_session(msg.Header, self.server_app.engines[self._testMethodName].session_settings)
            #self.server_app.engines[self._testMethodName].init_settings()
            return hb

        def register_hack(session_name):
            self.server_app.register_callback(session_name, None, self.server_app.on_queue_msg)
            self.server_app.engines[self._testMethodName].register_admin_callback(fix_messages_4_2_0_base.Logon, on_logon_hack, priority = CallbackRegistrar.CALLBACK_PRIORITY.FIRST + 
                        CallbackRegistrar.CALLBACK_PRIORITY.BEFORE)

        self.server_app.on_register_callbacks = register_hack
        self.server.start()
        self.client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        error = CLIENT_QUEUE.get(timeout=2)
        self.assertIsInstance(error, fix_errors.FIXInvalidFirstMessage)

    def tearDown(self):
        self.client.stop_all()
        self.server.stop_all()

        self.server_app.close_connection(self._testMethodName)
        self.client_app.close_connection(self._testMethodName)

        try:
            self.assertTrue(SERVER_QUEUE.empty())
            self.assertTrue(CLIENT_QUEUE.empty())
        finally:
            while not SERVER_QUEUE.empty(): SERVER_QUEUE.get()
            while not CLIENT_QUEUE.empty(): CLIENT_QUEUE.get()

            self.server_app.engines[self._testMethodName].store.clean_up()
            self.client_app.engines[self._testMethodName].store.clean_up()


if __name__ == "__main__":
    unittest.main()
