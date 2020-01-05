import unittest 
import asyncio

import fix_errors
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

        self.server_app = FIXTestAppServer()
        self.server = fix.SocketConnection(self.server_app, self.store, self.settings)
        self.server.start()

    def do_logout(self, client_app):
        client_app.engine.logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)



    """	Receive Logon<A> message"""
    """Respond with Logon<A> response message"""
    def test_valid_logon(self):
        client_app = FIXTestAppClient()
        client = fix.SocketConnection(client_app, self.store, self.settings_client)
        client.start()

        resp_logon = SERVER_QUEUE.get(timeout=2)
        sent_logon = CLIENT_QUEUE.get(timeout=2)

        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)

        self.do_logout(client_app)


    """If MsgSeqNum(34) is too high then send ResendRequest<2>"""
    def test_valid_logon_seq_high(self):
        client_app = FIXTestAppClient()
        client = fix.SocketConnection(client_app, self.store, self.settings_client)
        client_app.on_engine_initialized = lambda : setattr(client_app.engine, 'msg_seq_num_out', 10)
        client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(client_app)

    """Logon<A> message received with duplicate identity (i.e. same IP, port, SenderCompID, TargetCompID, etc. as existing connection)"""
    """Generate an "error" condition in test output"""
    """Disconnect without sending a message (note sending a Reject<3> or Logout would consume a MsgSeqNum)"""
    def test_dupe_logon(self):
        client_app = FIXTestAppClient()
        client = fix.SocketConnection(client_app, self.store, self.settings_client)
        client.start()

        client_app2 = FIXTestAppClient()
        client2 = fix.SocketConnection(client_app2, self.store, self.settings_client)
        resp_logon = SERVER_QUEUE.get(timeout=2)
        sent_logon = CLIENT_QUEUE.get(timeout=2)
        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)
        client2.start()

        error = SERVER_QUEUE.get(timeout=2)

        self.assertIsInstance(error, fix_errors.FIXSessionExistsError)

        self.do_logout(client_app)

    """Logon<A> message received with unauthenticated/non-configured identity """
    """(i.e. invalid SenderCompID, invalid TargetCompID, invalid source IP address, etc. vs. system configuration)"""
    """Generate an "error" condition in test output """
    """Disconnect without sending a message (note sending a Reject<3> or Logon<5> would consume a MsgSeqNum)"""
    def test_invalid_comp_ID(self):
        settings_bad_client = fix.SessionSettings([])
        settings_bad_client.read_dict({'SESSION1' : {'ConnectionType' : 'initiator',
            'BeginString' : 'FIX.4.2',
            'SenderCompID' : 'CLIENT1',
            'TargetCompID' : 'HOST',
            'SocketConnectPort' : '5001',
            'SocketConnectHost' : 'localhost',
            'FileStorePath' : ':memory:',
            'DataDictionary' : '../spec/FIX42.xml'}})

        client_bad = FIXTestAppClient()
        client_bad = fix.SocketConnection(client_bad, self.store, settings_bad_client)
        
        #self.server.start()
        client_bad.start()

        error = SERVER_QUEUE.get(timeout=2)
        self.assertIsInstance(error, fix_errors.FIXSessionNotFound)
        self.assertTrue(CLIENT_QUEUE.empty())


    """Invalid Logon<A> message
        Generate an "error" condition in test output
        (Optional) Send Reject<3> message with RefSeqNum(45) referencing Logon<A> message’s MsgSeqNum and with Text(58) referencing error condition
        Send Logout<5> message with Text(58) referencing error condition
        Disconnect
        """
    def test_invalid_logon(self):
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
        
        client_app = FIXTestAppClient()
        client = fix.SocketConnection(client_app, self.store, self.settings_client)

        async def send_logon_hack():
            client_app.engine._send(hb)

        def register_hack():
            client_app.register_callback(None, self.server_app.on_queue_msg)
            client_app.engine.send_logon = send_logon_hack

        client_app.on_register_callbacks = register_hack

        client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXInvalidFirstMessage)
        self.assertTrue(CLIENT_QUEUE.empty())

    """First message never received
        Disconnect
    """
    def test_no_first_message(self):
        client_app = FIXTestAppClient()
        client = fix.SocketConnection(client_app, self.store, self.settings_client)

        async def send_logon_hack():
            return

        def register_hack():
            client_app.register_callback(None, self.server_app.on_queue_msg)
            client_app.engine.send_logon = send_logon_hack

        client_app.on_register_callbacks = register_hack

        client.start()        
        self.assertIsInstance(SERVER_QUEUE.get(timeout=12), fix_errors.FIXHardKillError)
        self.assertTrue(CLIENT_QUEUE.empty())
        

    def tearDown(self):
        self.server.stop_all()
        try:
            self.assertTrue(SERVER_QUEUE.empty())
            self.assertTrue(CLIENT_QUEUE.empty())
        finally:
            while not SERVER_QUEUE.empty(): logging.error(f"Extra server message {SERVER_QUEUE.get()}")
            while not CLIENT_QUEUE.empty(): logging.error(f"Extra client message {CLIENT_QUEUE.get()}")



if __name__ == "__main__":
    unittest.main()
