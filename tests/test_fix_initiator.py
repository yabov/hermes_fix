import unittest 
import asyncio

import fix_errors
import fix_engine
import fix
import fix_messages_4_2_0_base
import logging
import queue

logging.basicConfig(level=logging.DEBUG, format= '%(levelname)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

SERVER_QUEUE = queue.Queue()
CLIENT_QUEUE = queue.Queue()

class FIXTestAppServer(fix.Application):
    def on_register_callbacks(self):
        self.register_callback(None, self.on_queue_msg)

    def on_queue_msg(self, msg):
        SERVER_QUEUE.put(msg)

    def on_error(self, error):
        SERVER_QUEUE.put(error)

class FIXTestAppClient(fix.Application):
    def on_register_callbacks(self):
        self.register_callback(None, self.on_queue_msg)

    def on_queue_msg(self, msg):
        CLIENT_QUEUE.put(msg)    

    def on_error(self, error):
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
                    'FileStorePath' : ':memory:',
                    'DataDictionary' : '../spec/FIX42.xml'}})

        self.settings_client  = fix.SessionSettings([])
        self.settings_client.read_dict({self._testMethodName : {'ConnectionType' : 'initiator',
            'BeginString' : 'FIX.4.2',
            'SenderCompID' : self._testMethodName,#'CLIENT',
            'TargetCompID' : 'HOST',
            'SocketConnectPort' : '5001',
            'SocketConnectHost' : 'localhost',
            'FileStorePath' : ':memory:',
            'DataDictionary' : '../spec/FIX42.xml'}})

        self.client_app = FIXTestAppClient()
        self.client = fix.SocketConnection(self.client_app, self.store, self.settings_client)
        self.server_app = FIXTestAppServer()
        self.server = fix.SocketConnection(self.server_app, self.store, self.settings)

    def do_logout(self, client_app):
        client_app.engine.logout()

        resp_logout = SERVER_QUEUE.get(timeout=5)
        sent_logout = CLIENT_QUEUE.get(timeout=5)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)

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
        self.server_app.on_engine_initialized = lambda : setattr(self.server_app.engine, 'msg_seq_num_out', 10)
        self.server.start()
        self.client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
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
        
        def on_logon_hack(msg):
            self.server_app.engine.settings = self.server_app.engine.find_session(msg.Header, self.server_app.engine.session_settings)
            self.server_app.engine.init_settings()
            return hb

        def register_hack():
            self.server_app.register_callback(None, self.server_app.on_queue_msg)
            self.server_app.register_callback(fix_messages_4_2_0_base.Logon, on_logon_hack, priority = fix_engine.CallbackWrapper.CALLBACK_PRIORITY.FIRST)

        self.server_app.on_register_callbacks = register_hack
        self.server.start()
        self.client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        error = CLIENT_QUEUE.get(timeout=2)
        self.assertIsInstance(error, fix_errors.FIXInvalidFirstMessage)


    def tearDown(self):
        #print("TearDown", self._testMethodName)
        self.server.stop_all()
        #print("Done", self._testMethodName)




if __name__ == "__main__":
    unittest.main()
