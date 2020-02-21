import logging
import queue
import unittest
from datetime import datetime, timedelta

import hermes_fix as fix
from hermes_fix import fix_engine, fix_errors
from hermes_fix.fix_callbacks import CallbackRegistrar
from hermes_fix.message_lib.FIX_4_2 import \
    fix_messages as fix_messages_4_2_0_base

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s-%(thread)d-%(asctime)s-%(filename)s:%(lineno)d - %(message)s')

SERVER_QUEUE = queue.Queue()
CLIENT_QUEUE = queue.Queue()


class FIXTestAppServer(fix.Application):
    def on_register_callbacks(self, session_name):
        super().on_register_callbacks(session_name)
        self.register_callback(session_name, None, self.on_queue_msg)

    def on_queue_msg(self, session_name, msg):
        SERVER_QUEUE.put(msg)

    def on_error(self, session_name, error):
        SERVER_QUEUE.put(error)


class FIXTestAppClient(fix.Application):
    def on_register_callbacks(self, session_name):
        super().on_register_callbacks(session_name)
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

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """MsgSeqNum(34) received as expected	
        Accept MsgSeqNum for the messagee"""

    def test_valid_msg(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.do_logout(self.client_app)

    """Respond with Resend Request<2> message"""

    def test_msg_seq_high(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.engines[self._testMethodName].msg_seq_num_out = 10

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.do_logout(self.client_app)

    """ MsgSeqNum(34) lower than expected without PossDupFlag(43) set to Y
    Exception: SeqReset-Reset
    Whenever possible it is recommended that FIX engine attempt to send a Logout message with a text message of "MsgSeqNum too low, expecting X but received Y"
    (optional) Wait for Logout message response (note likely will have inaccurate MsgSeqNum) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""

    def test_msg_seq_low(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.engines[self._testMethodName].store.new_day(
            datetime.utcnow())
        self.client_app.engines[self._testMethodName].store.set_current_in_seq(
            1)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 1

        self.client_app.send_message(self._testMethodName, order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXSequenceTooLowError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        #self.assertIsInstance(SERVER_QUEUE.get(timeout=3), fix_errors.FIXSequenceTooLowError)
        #self.assertIsInstance(SERVER_QUEUE.get(timeout=3), fix_errors.FIXHardKillError)

    """ Garbled message received	
        Consider garbled and ignore message (do not increment inbound MsgSeqNum) and continue accepting messages
        Generate a "warning" condition in test output"""

    def test_garbled_msg(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'+'\x01'+'BORKED'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXGarbledMessageError)

        # self.do_logout(self.client_app)
        self.client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """ PossDupFlag(43) set to Y; OrigSendingTime(122) specified is less than or equal to SendingTime(52) and MsgSeqNum(34) lower than expected
    Note: OrigSendingTime should be earlier than SendingTime unless the message is being resent within the same second during which it was sent
    Check to see if MsgSeqNum has already been received
    If already received then ignore the message, otherwise accept and process the message"""

    def test_poss_dupe_discard(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.OrigSendingTime = order_msg.TransactTime
        order_msg.Header.PossDupFlag = 'Y'

        self.client_app.engines[self._testMethodName].store.new_day(
            datetime.utcnow())
        self.client_app.engines[self._testMethodName].store.set_current_in_seq(
            1)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 1

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXDupeMessageRecv)

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
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.OrigSendingTime = (
            datetime.utcnow() + timedelta(hours=1)).strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.Header.PossDupFlag = 'Y'

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXSendTimeAccuracyError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        sent_logout = CLIENT_QUEUE.get(timeout=3)
        resp_logout = SERVER_QUEUE.get(timeout=3)

        self.assertIsInstance(resp_logout, fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(sent_logout, fix_messages_4_2_0_base.Logout)

    """ PossDupFlag(43) set to Y and OrigSendingTime(122) not specified
    Note: Always set OrigSendingTime to the time when the message was originally sent-not the present SendingTime and set PossDupFlag = "Y" when responding to a Resend Request
    Send Reject<3> (session-level) message referencing missing OrigSendingTime(122) (≥ FIX 4.2: SessionRejectReason(373) = 1 - "Required tag missing")
    Increment inbound MsgSeqNum"""

    def test_send_time_missing(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.PossDupFlag = 'Y'

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.RequiredTagMissingError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ BeginString(8) value received as expected and specified in testing profile and matches BeginString on outbound messages	
    Accept BeginString for the message"""

    def test_begin_string_valid(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.Header.BeginString = 'FIX.4.2'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.do_logout(self.client_app)

    """BeginString(8) value (e.g. "FIX.4.2") received did not match value expected and specified in testing profile or does not match BeginString on outbound messages	
    Send Logout<5> message referencing incorrect BeginString value
    (optional) Wait for Logout<5> message response (note likely will have incorrect BeginString) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""

    def test_begin_string_invalid(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.Header.BeginString = 'FIX.BAD'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageError)

        sent_logout = CLIENT_QUEUE.get(timeout=3)
        resp_logout = SERVER_QUEUE.get(timeout=3)

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
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.Header.SenderCompID = 'BAD_SENDER'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXBadCompIDError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """ SenderCompID(49) and TargetCompID(56) values received did not match values expected and specified in testing profile	
    Send Reject<3> (session-level) message referencing invalid SenderCompID or TargetCompID (≥ FIX 4.2: SessionRejectReason(373) = 9 - "CompID problem")
    Increment inbound MsgSeqNum(34)
    Send Logout<5> message referencing incorrect SenderCompID or TargetCompID value
    (optional) Wait for Logout<5> message response (note likely will have incorrect SenderCompID or TargetCompID) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""

    def test_bad_target(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.Header.TargetCompID = 'BAD_TARGET'
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXBadCompIDError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """BodyLength(9) value received is not correct.	
    Consider garbled and ignore message (do not increment inbound MsgSeqNum(34)) and continue accepting messages
    Generate a "warning" condition in test output"""

    def test_bad_body_len(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.Header.BodyLength = 999
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=5),
                              fix_errors.FIXGarbledMessageError)
        for _ in range(11):
            self.assertIsInstance(SERVER_QUEUE.get(
                timeout=3), fix_errors.FIXGarbledMessageError)

        self.client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """SendingTime(52 value received is either not specified in UTC (Universal Time Coordinated also known as GMT) or is not within a reasonable time (e.g. 2 minutes) of atomic clock-based time.
    Rationale: Verify system clocks on both sides are in sync and that SendingTime must be current time
    Send Reject<3> (session-level) message referencing inaccurate SendingTime (≥ FIX 4.2: SessionRejectReason(373) = 10 - "SendingTime accuracy problem")
    Increment inbound MsgSeqNum(34)
    Send Logout<5> message referencing inaccurate SendingTime value
    (optional) Wait for Logout<5> message response (note likely will have inaccurate SendingTime) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output."""

    def test_send_time_late(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        order_msg.Header.SendingTime = (
            datetime.utcnow() + timedelta(hours=1)).strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXSendTimeAccuracyError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """MsgType(35) value received is not valid (defined in spec or classified as user-defined)	
    Send Reject<3> (session-level) message referencing invalid MsgType (≥ FIX 4.2: SessionRejectReason(373) = 11 - "Invalid MsgType")
    Increment inbound MsgSeqNum(34)
    Generate a "warning" condition in test output"""

    def test_bad_msg_type(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()

        fix_messages_4_2_0_base.OrderSingle._msgtype = 'BAD'

        class String_Type(str):
            def __bytes__(self):
                return str(self).encode()

        class MsgType(String_Type):
            _tag = '35'

        order_msg.Header.register_field(MsgType, True)

        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.client_app.send_message(self._testMethodName, order_msg)

        fix_messages_4_2_0_base.OrderSingle._msgtype = 'D'

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageTypeError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)
        self.do_logout(self.client_app)

    """MsgType(35) value received is valid (defined in spec or classified as user-defined) but not supported or registered in testing profile	
    If < FIX 4.2
    Send Reject<3> (session-level) message referencing valid but unsupported MsgType
    If ≥ FIX 4.2
    Send Business Message Reject<j> message referencing valid but unsupported MsgType (≥ FIX 4.2: BusinessRejectReason(380) = 3 - "Unsupported Message Type")
    Increment inbound MsgSeqNum(34)
    Generate a "warning" condition in test output"""

    def test_unsupported_msg(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.server_app.engines[self._testMethodName].callback_register = CallbackRegistrar(
            self.server_app.engines[self._testMethodName].loop)

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXUnsupportedMessageTypeError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.BusinessMessageReject)

        self.server_app.register_callback(
            self._testMethodName, None,  self.server_app.on_queue_msg)

        self.do_logout(self.client_app)

    """Message to send/queue while disconnected	
    Queue outgoing messages. Note there are two valid approaches:

    Queue without regards to MsgSeqNum(34)
    Store data for messages
    Queue each message with the next MsgSeqNum value
    Store data for messages in such a manner as to use and "consume" the next MsgSeqNum(34)
    Note: SendingTime(52): must contain the time the message is sent not the time the message was queued"""

    def test_queue_msg(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')

        self.do_logout(self.client_app)

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=4),
                              fix_messages_4_2_0_base.Logon)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=4),
                              fix_messages_4_2_0_base.Logon)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.do_logout(self.client_app)

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
