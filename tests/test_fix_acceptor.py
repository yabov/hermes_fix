import logging
import queue
import unittest
from datetime import datetime, timedelta

import hermes_fix as fix
from hermes_fix import fix_errors
from hermes_fix.message_lib.FIX_4_2 import \
    fix_messages as fix_messages_4_2_0_base

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

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


class Test(unittest.TestCase):
    def setUp(self):
        #print("Entering", self._testMethodName)
        self.store = fix.FileStoreFactory()
        self.settings = fix.SessionSettings([])
        self.settings.read_dict({self._testMethodName: {'ConnectionType': 'acceptor',
                                                        'BeginString': 'FIX.4.2',
                                                        'SenderCompID': 'HOST',
                                                        'TargetCompID': self._testMethodName,  # 'CLIENT',
                                                        'SocketAcceptPort': '5001',
                                                        'StorageConnectionString': 'sqlite:///:memory:?check_same_thread=False',
                                                        'DataDictionary': '../spec/FIX42.xml',
                                                        'ConnectionStartTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                        'ConnectionEndTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                        'LogonTime': (datetime.utcnow() - timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                        'LogoutTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S')}})

        self.settings_client = fix.SessionSettings([])
        self.settings_client.read_dict({self._testMethodName: {'ConnectionType': 'initiator',
                                                               'BeginString': 'FIX.4.2',
                                                               'SenderCompID': self._testMethodName,  # 'CLIENT',
                                                               'TargetCompID': 'HOST',
                                                               'SocketConnectPort': '5001',
                                                               'SocketConnectHost': 'localhost',
                                                               'StorageConnectionString': 'sqlite:///:memory:?check_same_thread=False',
                                                               'DataDictionary': '../spec/FIX42.xml',
                                                               'ConnectionStartTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                               'ConnectionEndTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                               'LogonTime': (datetime.utcnow() - timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                               'LogoutTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S')}})

        self.client_app = FIXTestAppClient()
        self.client = fix.SocketConnection(
            self.client_app, self.store, self.settings_client)

        self.server_app = FIXTestAppServer()
        self.server = fix.SocketConnection(
            self.server_app, self.store, self.settings)
        self.server.start()

    def do_logout(self, client_app):
        client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """	Receive Logon<A> message"""
    """Respond with Logon<A> response message"""

    def test_valid_logon(self):
        self.client.start()

        resp_logon = SERVER_QUEUE.get(timeout=3)
        sent_logon = CLIENT_QUEUE.get(timeout=3)

        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)

        self.do_logout(self.client_app)

    """If MsgSeqNum(34) is too high then send ResendRequest<2>"""

    def test_valid_logon_seq_high(self):

        def register_hack(session_name):
            self.client_app.register_callback(
                session_name, None, self.client_app.on_queue_msg)
            self.client_app.engines[session_name].msg_seq_num_out = 10

        self.client_app.on_register_callbacks = register_hack
        self.client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(self.client_app)

    """Logon<A> message received with duplicate identity (i.e. same IP, port, SenderCompID, TargetCompID, etc. as existing connection)"""
    """Generate an "error" condition in test output"""
    """Disconnect without sending a message (note sending a Reject<3> or Logout would consume a MsgSeqNum)"""

    def test_dupe_logon(self):
        self.client.start()

        settings_client2 = fix.SessionSettings([])
        settings_client2.read_dict({self._testMethodName: {'ConnectionType': 'initiator',
                                                           'BeginString': 'FIX.4.2',
                                                           'SenderCompID': self._testMethodName,  # 'CLIENT',
                                                           'TargetCompID': 'HOST',
                                                           'SocketConnectPort': '5001',
                                                           'SocketConnectHost': 'localhost',
                                                           'StorageConnectionString': 'sqlite:///:memory:?check_same_thread=False',
                                                           'DataDictionary': '../spec/FIX42.xml',
                                                           'ConnectionStartTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                           'ConnectionEndTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                           'LogonTime': (datetime.utcnow() - timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                           'LogoutTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S')}})

        client_app2 = FIXTestAppClient()
        client2 = fix.SocketConnection(
            client_app2, self.store, settings_client2)
        resp_logon = SERVER_QUEUE.get(timeout=3)
        sent_logon = CLIENT_QUEUE.get(timeout=3)
        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)
        client2.start()

        error = SERVER_QUEUE.get(timeout=3)

        self.assertIsInstance(error, fix_errors.FIXSessionExistsError)

        self.do_logout(self.client_app)
        client_app2.close_connection(self._testMethodName)

    """Logon<A> message received with unauthenticated/non-configured identity """
    """(i.e. invalid SenderCompID, invalid TargetCompID, invalid source IP address, etc. vs. system configuration)"""
    """Generate an "error" condition in test output """
    """Disconnect without sending a message (note sending a Reject<3> or Logon<5> would consume a MsgSeqNum)"""

    def test_invalid_comp_ID(self):
        settings_bad_client = fix.SessionSettings([])
        settings_bad_client.read_dict({'SESSION1': {'ConnectionType': 'initiator',
                                                    'BeginString': 'FIX.4.2',
                                                    'SenderCompID': 'CLIENT1',
                                                    'TargetCompID': 'HOST',
                                                    'SocketConnectPort': '5001',
                                                    'SocketConnectHost': 'localhost',
                                                    'StorageConnectionString': 'sqlite:///:memory:?check_same_thread=False',
                                                    'DataDictionary': '../spec/FIX42.xml',
                                                    'ConnectionStartTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                    'ConnectionEndTime': (datetime.utcnow() + + timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                    'LogonTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                    'LogoutTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S')}})

        client_bad_app = FIXTestAppClient()
        client_bad = fix.SocketConnection(
            client_bad_app, self.store, settings_bad_client)

        # self.server.start()
        client_bad.start()

        error = SERVER_QUEUE.get(timeout=3)
        self.assertIsInstance(error, fix_errors.FIXSessionNotFound)
        self.assertTrue(CLIENT_QUEUE.empty())
        client_bad_app.close_connection(self._testMethodName)
        client_bad.stop_all()

    """Invalid Logon<A> message
        Generate an "error" condition in test output
        (Optional) Send Reject<3> message with RefSeqNum(45) referencing Logon<A> message’s MsgSeqNum and with Text(58) referencing error condition
        Send Logout<5> message with Text(58) referencing error condition
        Disconnect
        """
    # def test_invalid_logon(self):
    #    pass
    # need to implement passwords and other checks

    """First message received is not a Logon<A> message.	
        Log an error “first message not a logon”
        Disconnect
    """

    def test_invalid_first_message(self):
        hb = fix_messages_4_2_0_base.Heartbeat()
        hb.Header.BeginString = 'FIX.4.2'
        hb.Header.SenderCompID = self._testMethodName
        hb.Header.TargetCompID = 'HOST'
        hb.Header.MsgSeqNum = 1

        def send_logon_hack():
            self.client_app.engines[self._testMethodName]._send(hb)

        def register_hack(session_name):
            self.client_app.register_callback(
                session_name, None, self.client_app.on_queue_msg)
            self.client_app.engines[session_name].send_logon = send_logon_hack

        self.client_app.on_register_callbacks = register_hack

        self.client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidFirstMessage)

    """First message never received
        Disconnect
    """

    def test_no_first_message(self):
        def send_logon_hack():
            return

        def register_hack(session_name):
            self.client_app.register_callback(
                session_name, None, self.client_app.on_queue_msg)
            self.client_app.engines[session_name].send_logon = send_logon_hack

        self.client_app.on_register_callbacks = register_hack

        self.client.start()
        self.assertIsInstance(SERVER_QUEUE.get(
            timeout=12), fix_errors.FIXHardKillError)
        self.assertTrue(CLIENT_QUEUE.empty())

    def tearDown(self):
        self.client.stop_all()
        self.server.stop_all()

        self.server_app.close_connection(self._testMethodName)
        self.client_app.close_connection(self._testMethodName)

        try:
            self.assertTrue(SERVER_QUEUE.empty())
            self.assertTrue(CLIENT_QUEUE.empty())
        finally:
            while not SERVER_QUEUE.empty():
                SERVER_QUEUE.get()
            while not CLIENT_QUEUE.empty():
                CLIENT_QUEUE.get()

            if self._testMethodName in self.server_app.engines:
                self.server_app.engines[self._testMethodName].store.clean_up()
            if self._testMethodName in self.client_app.engines:
                self.client_app.engines[self._testMethodName].store.clean_up()


if __name__ == "__main__":
    unittest.main()
