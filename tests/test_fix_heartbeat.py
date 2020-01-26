import unittest 
import asyncio

import logging
import queue
from datetime import datetime, timedelta
import time

from .. import fix_errors
from .. import fix
from .. import fix_engine
from ..message_lib.FIX_4_2 import fix_messages as fix_messages_4_2_0_base
from ..fix_callbacks import CallbackRegistrar


logging.basicConfig(level=logging.DEBUG, format= '%(levelname)s-%(asctime)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

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
                    'HeartBeatInt' : '1',
                    'HeatBeatGracePeriod' : '1.5',
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
            'HeartBeatInt' : '1',
            'HeatBeatGracePeriod' : '1.5',
            'DataDictionary' : '../spec/FIX42.xml',
            'ConnectionStartTime' : datetime.utcnow().time().strftime('%H:%M:%S'),
            'ConnectionEndTime' : (datetime.utcnow() + timedelta(seconds = 10)).time().strftime('%H:%M:%S'),
            'LogonTime': (datetime.utcnow() - timedelta(seconds=10)).time().strftime('%H:%M:%S'),
            'LogoutTime' : (datetime.utcnow() + timedelta(seconds = 10)).time().strftime('%H:%M:%S')}})

        self.client_app = FIXTestAppClient()
        self.client = fix.SocketConnection(self.client_app, self.store, self.settings_client)
        self.server_app = FIXTestAppServer()
        self.server = fix.SocketConnection(self.server_app, self.store, self.settings)

        self.server.start()
        self.client.start()

        resp_logon = SERVER_QUEUE.get(timeout=2)
        sent_logon = CLIENT_QUEUE.get(timeout=2)
        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)

    def do_logout(self, client_app):
        client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)

    """No data sent during preset heartbeat interval (HeartBeatInt(108) field)	
    Send Heartbeat message"""
    def test_valid_msg(self):
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        #waiting for 2nd heartbeat
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)
        self.do_logout(self.client_app)

    """Data sent during preset heartbeat interval (HeartBeatInt(108) field)	
    skip Heartbeat message"""
    def test_msg_instead_of_hb(self):
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        time.sleep(.5)

        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        self.client_app.send_message(self._testMethodName, order_msg)

        #waiting for 2nd heartbeat
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.OrderSingle)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)
        self.do_logout(self.client_app)

    """No Heartbeat during preset interval
    send TestMessage"""
    def test_msg_no_hb(self):
        self.server_app.engines[self._testMethodName].out_heart_beat_int = 10
        future_out = asyncio.run_coroutine_threadsafe(self.server_app.engines[self._testMethodName].schedule_next_out_beat_await(), self.server_app.engines[self._testMethodName].loop)
        future_out.result()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.do_logout(self.client_app)

    """No Test Message response
    Logout"""
    def test_no_response_to_test_msg(self):
        self.server_app.engines[self._testMethodName].out_heart_beat_int = 10
        self.server_app.engines[self._testMethodName].in_heart_beat_int = 10
        future_out = asyncio.run_coroutine_threadsafe(self.server_app.engines[self._testMethodName].schedule_next_out_beat_await(), self.server_app.engines[self._testMethodName].loop)
        future_out.result()

        def on_test_msg(session, msg):
            raise fix_errors.FIXRejectError(1, '1', '1', 'TestReject', 1)


        self.server_app.engines[self._testMethodName].register_admin_callback(fix_messages_4_2_0_base.TestRequest, on_test_msg, CallbackRegistrar.CALLBACK_PRIORITY.NORMAL -1)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXRejectError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)


        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
    
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
