import asyncio
import logging
import queue
import time
import unittest
from datetime import datetime, timedelta

import hermes_fix as fix
from hermes_fix import fix_engine, fix_errors
from hermes_fix.message_lib.FIX_4_2 import \
    fix_messages as fix_messages_4_2_0_base

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s-%(asctime)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

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
                                                        'StorageConnectionString': f'sqlite:///store/{self._testMethodName}.server.db?check_same_thread=False',
                                                        'ConnectionStartTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                        'ConnectionEndTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                        'LogonTime': (datetime.utcnow() + timedelta(seconds=6)).time().strftime('%H:%M:%S'),
                                                        'LogoutTime': (datetime.utcnow() + timedelta(seconds=5)).time().strftime('%H:%M:%S')}})

        self.settings_client = fix.SessionSettings([])
        self.settings_client.read_dict({self._testMethodName: {'ConnectionType': 'initiator',
                                                               'BeginString': 'FIX.4.2',
                                                               'SenderCompID': self._testMethodName,  # 'CLIENT',
                                                               'TargetCompID': 'HOST',
                                                               'SocketConnectPort': '5001',
                                                               'SocketConnectHost': 'localhost',
                                                               'StorageConnectionString': f'sqlite:///store/{self._testMethodName}.client.db?check_same_thread=False',
                                                                      'ConnectionStartTime': datetime.utcnow().time().strftime('%H:%M:%S'),
                                                               'ConnectionEndTime': (datetime.utcnow() + timedelta(seconds=10)).time().strftime('%H:%M:%S'),
                                                               'LogonTime': (datetime.utcnow() + timedelta(seconds=6)).time().strftime('%H:%M:%S'),
                                                               'LogoutTime': (datetime.utcnow() + timedelta(seconds=3)).time().strftime('%H:%M:%S')}})

        self.client_app = FIXTestAppClient()
        self.client = fix.SocketConnection(
            self.client_app, self.store, self.settings_client)
        self.server_app = FIXTestAppServer()
        self.server = fix.SocketConnection(
            self.server_app, self.store, self.settings)

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

    """ start session in logged on state, wait for logout, ensure new day is performed and logon happens with reset sequence numbers"""

    def test_new_day(self):

        self.server.start()
        self.client.start()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logon)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logon)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5),
                              fix_messages_4_2_0_base.Logon)

        self.do_logout(self.client_app)

    def tearDown(self):
        self.server_app.close_connection(self._testMethodName)
        self.client_app.close_connection(self._testMethodName)

        self.client.stop_all()
        self.server.stop_all()

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
