import unittest
import asyncio

import logging
import queue
from datetime import datetime, timedelta

from hermes_fix import fix_errors
from hermes_fix import fix
from hermes_fix import fix_engine
from hermes_fix.message_lib.FIX_4_2 import fix_messages as fix_messages_4_2_0_base


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

    def on_error(self, session_name, error):
        CLIENT_QUEUE.put(error)


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
        self.client.start()

        resp_logon = SERVER_QUEUE.get(timeout=3)
        sent_logon = CLIENT_QUEUE.get(timeout=3)
        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)

    def do_logout(self, client_app):
        client_app.engines[self._testMethodName].logout()

        resp_logout = SERVER_QUEUE.get(timeout=5)
        sent_logout = CLIENT_QUEUE.get(timeout=5)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)

    """Invalid CheckSum(10)	
    Consider garbled and ignore message (do not increment inbound MsgSeqNum(34)) and continue accepting messages
    Generate a "warning" condition in test output
    """

    def test_bad_checksum(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.Trailer.CheckSum = '000'

        self.client_app.send_message(self._testMethodName, order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXGarbledMessageError)

        self.client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logout)

    """Invalid CheckSum(10)	
    Consider garbled and ignore message (do not increment inbound MsgSeqNum(34)) and continue accepting messages
    Generate a "warning" condition in test output
    """

    def test_checksum_not_last(self):
        class CheckSum(str):
            _tag = '10'

            def __init__(self, *args, **kwargs):
                super().__init__()
                self._tag = '8'

        order_msg = fix_messages_4_2_0_base.OrderSingle()

        # hack the tag to not send checksum
        order_msg.Trailer.register_field(CheckSum, True)

        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXGarbledMessageError)

        self.client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logout)

    """Invalid CheckSum(10)	
    Consider garbled and ignore message (do not increment inbound MsgSeqNum(34)) and continue accepting messages
    Generate a "warning" condition in test output
    """

    def test_checksum_not_3(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.Trailer.CheckSum = '00000'

        self.client_app.send_message(self._testMethodName, order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXGarbledMessageError)

        self.client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logout)

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

            self.server_app.engines[self._testMethodName].store.clean_up()
            self.client_app.engines[self._testMethodName].store.clean_up()


if __name__ == "__main__":
    unittest.main()
