import unittest 
import asyncio

import fix_errors
import fix
import fix_messages_4_2_0_base
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

    """MsgSeqNum(34) received as expected	
        Accept MsgSeqNum for the messagee"""
    def test_valid_msg(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.NewOrderSingle)

        self.do_logout(self.client_app)
        
    
    """Respond with Resend Request<2> message"""
    def test_msg_seq_high(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.engine.msg_seq_num_out = 10

        self.client_app.send_message(order_msg)
        
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.SequenceReset)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.NewOrderSingle)

        self.do_logout(self.client_app)

    """ MsgSeqNum(34) lower than expected without PossDupFlag(43) set to Y
    Exception: SeqReset-Reset
    Whenever possible it is recommended that FIX engine attempt to send a Logout message with a text message of "MsgSeqNum too low, expecting X but received Y"
    (optional) Wait for Logout message response (note likely will have inaccurate MsgSeqNum) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""
    def test_msg_seq_low(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.engine.msg_seq_num_out = 0

        self.client_app.send_message(order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXSequenceTooLowError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXSequenceTooLowError)
        #self.assertIsInstance(SERVER_QUEUE.get(timeout=3), fix_engine.FIXSessionLogoutTimeoutWarning)

        

    """ Garbled message received	
        Consider garbled and ignore message (do not increment inbound MsgSeqNum) and continue accepting messages
        Generate a "warning" condition in test output"""
    def test_garbled_msg(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'+'\x01'+'BORKED'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXGarbledMessageError)

        #self.do_logout(self.client_app)
        self.client_app.engine.logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_messages_4_2_0_base.SequenceReset)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)

    """ PossDupFlag(43) set to Y; OrigSendingTime(122) specified is less than or equal to SendingTime(52) and MsgSeqNum(34) lower than expected
    Note: OrigSendingTime should be earlier than SendingTime unless the message is being resent within the same second during which it was sent
    Check to see if MsgSeqNum has already been received
    If already received then ignore the message, otherwise accept and process the message"""
    def test_poss_dupe_discard(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.OrigSendingTime = order_msg.TransactTime
        order_msg.Header.PossDupFlag = fix_messages_4_2_0_base.PossDupFlag.ENUM_YES

        self.client_app.engine.msg_seq_num_out -= 1

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXDupeMessageRecv)

        self.do_logout(self.client_app)


    """ PossDupFlag(43) set to Y; OrigSendingTime(122) specified is greater than SendingTime(52) and MsgSeqNum(34) as expected

    Note: OrigSendingTime should be earlier than SendingTime unless the message is being resent within the same second during which it was sent

    Send Reject<3> (session-level) message referencing inaccurate SendingTime (≥ FIX 4.2: SessionRejectReason(373) = 10 - "SendingTime accuracy problem")
    Increment inbound MsgSeqNum
    Optional:
    Send Logout<5> message referencing inaccurate SendingTime value
    (optional) Wait for Logout<5> message response (note likely will have inaccurate SendingTime) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output."""
    def test_send_time_accuracy(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.OrigSendingTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.Header.PossDupFlag = fix_messages_4_2_0_base.PossDupFlag.ENUM_YES

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXSendTimeAccuracyError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)

        sent_logout = CLIENT_QUEUE.get(timeout=5)
        resp_logout = SERVER_QUEUE.get(timeout=5)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)


    """ PossDupFlag(43) set to Y and OrigSendingTime(122) not specified
    Note: Always set OrigSendingTime to the time when the message was originally sent-not the present SendingTime and set PossDupFlag = "Y" when responding to a Resend Request
    Send Reject<3> (session-level) message referencing missing OrigSendingTime(122) (≥ FIX 4.2: SessionRejectReason(373) = 1 - "Required tag missing")
    Increment inbound MsgSeqNum"""
    def test_send_time_missing(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.PossDupFlag = fix_messages_4_2_0_base.PossDupFlag.ENUM_YES

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.RequiredTagMissingError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ BeginString(8) value received as expected and specified in testing profile and matches BeginString on outbound messages	
    Accept BeginString for the message"""
    def test_begin_string_valid(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.Header.BeginString = 'FIX.4.2'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.NewOrderSingle)

        self.do_logout(self.client_app)

    """BeginString(8) value (e.g. "FIX.4.2") received did not match value expected and specified in testing profile or does not match BeginString on outbound messages	
    Send Logout<5> message referencing incorrect BeginString value
    (optional) Wait for Logout<5> message response (note likely will have incorrect BeginString) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""
    def test_begin_string_invalid(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.Header.BeginString = 'FIX.BAD'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXInvalidMessageError)

        sent_logout = CLIENT_QUEUE.get(timeout=5)
        resp_logout = SERVER_QUEUE.get(timeout=5)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)

    """ SenderCompID(49) and TargetCompID(56) values received did not match values expected and specified in testing profile	
    Send Reject<3> (session-level) message referencing invalid SenderCompID or TargetCompID (≥ FIX 4.2: SessionRejectReason(373) = 9 - "CompID problem")
    Increment inbound MsgSeqNum(34)
    Send Logout<5> message referencing incorrect SenderCompID or TargetCompID value
    (optional) Wait for Logout<5> message response (note likely will have incorrect SenderCompID or TargetCompID) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""
    def test_bad_sender(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.Header.SenderCompID = 'BAD_SENDER'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXBadCompIDError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)


        sent_logout = CLIENT_QUEUE.get(timeout=5)
        resp_logout = SERVER_QUEUE.get(timeout=5)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)

    """ SenderCompID(49) and TargetCompID(56) values received did not match values expected and specified in testing profile	
    Send Reject<3> (session-level) message referencing invalid SenderCompID or TargetCompID (≥ FIX 4.2: SessionRejectReason(373) = 9 - "CompID problem")
    Increment inbound MsgSeqNum(34)
    Send Logout<5> message referencing incorrect SenderCompID or TargetCompID value
    (optional) Wait for Logout<5> message response (note likely will have incorrect SenderCompID or TargetCompID) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""
    def test_bad_target(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.Header.TargetCompID = 'BAD_TARGET'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXBadCompIDError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)


        sent_logout = CLIENT_QUEUE.get(timeout=5)
        resp_logout = SERVER_QUEUE.get(timeout=5)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)

    """BodyLength(9) value received is not correct.	
    Consider garbled and ignore message (do not increment inbound MsgSeqNum(34)) and continue accepting messages
    Generate a "warning" condition in test output"""
    def test_bad_body_len(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.Header.BodyLength = 999
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_errors.FIXGarbledMessageError)
        for _ in range(10):
            self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_errors.FIXGarbledMessageError)

        self.client_app.engine.logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.NewOrderSingle)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=5), fix_messages_4_2_0_base.Logout)

    """SendingTime(52 value received is either not specified in UTC (Universal Time Coordinated also known as GMT) or is not within a reasonable time (e.g. 2 minutes) of atomic clock-based time.
    Rationale: Verify system clocks on both sides are in sync and that SendingTime must be current time
    Send Reject<3> (session-level) message referencing inaccurate SendingTime (≥ FIX 4.2: SessionRejectReason(373) = 10 - "SendingTime accuracy problem")
    Increment inbound MsgSeqNum(34)
    Send Logout<5> message referencing inaccurate SendingTime value
    (optional) Wait for Logout<5> message response (note likely will have inaccurate SendingTime) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output."""
    def test_send_time_late(self):
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.SendingTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXSendTimeAccuracyError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)
        self.do_logout(self.client_app)

    """MsgType(35) value received is not valid (defined in spec or classified as user-defined)	
    Send Reject<3> (session-level) message referencing invalid MsgType (≥ FIX 4.2: SessionRejectReason(373) = 11 - "Invalid MsgType")
    Increment inbound MsgSeqNum(34)
    Generate a "warning" condition in test output"""
    def test_bad_msg_type(self):
        fix_messages_4_2_0_base.NewOrderSingle._msgtype = 'BAD'
        order_msg = fix_messages_4_2_0_base.NewOrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = fix_messages_4_2_0_base.HandlInst.ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION
        order_msg.Symbol = 'AAPL'
        order_msg.Side = fix_messages_4_2_0_base.Side.ENUM_BUY
        order_msg.TransactTime = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(order_msg)

        fix_messages_4_2_0_base.NewOrderSingle._msgtype = 'D'

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXInvalidMessageTypeError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)
        self.do_logout(self.client_app)

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
