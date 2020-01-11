import unittest 
import asyncio

import fix_errors
import fix
import message_lib.FIX_4_2.fix_messages as fix_messages_4_2_0_base
import logging
import queue
import datetime

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

        self.server.start()
        self.client.start()

        resp_logon = SERVER_QUEUE.get(timeout=2)
        sent_logon = CLIENT_QUEUE.get(timeout=2)
        self.assertIsInstance(resp_logon, fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(sent_logon, fix_messages_4_2_0_base.Logon)



    def do_logout(self, client_app):
        client_app.engine.logout()

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
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.Trailer.CheckSum = '000'

        self.client_app.send_message(order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXGarbledMessageError)

        self.client_app.engine.logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.OrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)

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

        order_msg.Trailer.register_field(CheckSum, True) #hack the tag to not send checksum

        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXGarbledMessageError)

        self.client_app.engine.logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.OrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)
        
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
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.Trailer.CheckSum = '00000'

        self.client_app.send_message(order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXGarbledMessageError)

        self.client_app.engine.logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.OrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)

        
    def tearDown(self):
        self.server.stop_all()
        try:
            self.assertTrue(SERVER_QUEUE.empty())
            self.assertTrue(CLIENT_QUEUE.empty())
        finally:
            while not SERVER_QUEUE.empty(): SERVER_QUEUE.get()
            while not CLIENT_QUEUE.empty(): CLIENT_QUEUE.get()
        




if __name__ == "__main__":
    unittest.main()
