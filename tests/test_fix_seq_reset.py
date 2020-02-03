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

    """Receive Sequence Reset (Gap Fill) message with NewSeqNo(36) > MsgSeqNum(34) and MsgSeqNum > than expect sequence number	
    Issue Resend Request<2> to fill gap between last expected MsgSeqNum & received MsgSeqNum"""

    def test_reset_high(self):
        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 10
        reset_msg.GapFillFlag = 'Y'
        reset_msg.Header.MsgSeqNum = 5

        self.client_app.send_message(self._testMethodName, reset_msg)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 10

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXEngineResendRequest)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.ResendRequest)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        #self.assertIsInstance(CLIENT_QUEUE.get(timeout=3), fix_messages_4_2_0_base.ResendRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(self.client_app)

    """Receive Sequence Reset (Gap Fill)<4> message with NewSeqNo(36) > MsgSeqNum(34) and MsgSeqNum = to expected sequence number	
    Set next expected sequence number = NewSeqNo"""

    def test_reset_normal(self):
        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 10
        reset_msg.GapFillFlag = 'Y'

        self.client_app.send_message(self._testMethodName, reset_msg)

        self.client_app.engines[self._testMethodName].msg_seq_num_out = 10

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(self.client_app)

    """ Receive Sequence Reset (Gap Fill)<4> message with NewSeqNo(36) > MsgSeqNum(34) and MsgSeqNum < than expected sequence number and PossDupFlag(43) = "Y"	
    Ignore message"""

    def test_reset_drop_msg(self):

        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 10
        reset_msg.Header.PossDupFlag = 'Y'
        reset_msg.Header.OrigSendingTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        reset_msg.Header.MsgSeqNum = 1
        reset_msg.GapFillFlag = 'Y'

        self.client_app.send_message(self._testMethodName, reset_msg)

        self.client_app.engines[self._testMethodName].store.new_day(
            datetime.utcnow())
        self.client_app.engines[self._testMethodName].store.set_current_in_seq(
            1)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 2
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXDropMessageError)

        self.do_logout(self.client_app)

    """Receive Sequence Reset (Gap Fill)<4> message with NewSeqNo(36) > MsgSeqNum(34) and MsgSeqNum < than expected sequence number and without PossDupFlag(43) = "Y"	
    If possible send a Logout<5> message with text of "MsgSeqNum too low, expecting X received Y", prior to disconnecting FIX session
    (optional) Wait for Logout message response (note likely will have inaccurate MsgSeqNum) or wait 2 seconds whichever comes first
    Disconnect
    Generate an "error" condition in test output"""

    def test_reset_too_low(self):

        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 10
        reset_msg.Header.MsgSeqNum = 1
        reset_msg.GapFillFlag = 'Y'

        self.client_app.send_message(self._testMethodName, reset_msg)

        self.client_app.engines[self._testMethodName].msg_seq_num_out = 2

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXSequenceTooLowError)

        # self.client_app.engines[self._testMethodName].logout()

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    """ Receive Sequence Reset (Gap Fill)<4> message with NewSeqNo(36) ≤ MsgSeqNum(34) and MsgSeqNum = to expected sequence number	
    Send Reject<3> (session-level) message with message "attempt to lower sequnce number, invalid value NewSeqNum=<x>" """

    def test_new_seq_too_low(self):

        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 0
        reset_msg.GapFillFlag = 'Y'

        self.client_app.send_message(self._testMethodName, reset_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXResetSequenceToLowerError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """Receive Sequence Reset (reset) message with NewSeqNo(36) > than expected sequence number	
    Accept the Sequence Reset (Reset) message without regards to its MsgSeqNum(34)
    Set expected sequence number equal to NewSeqNo"""

    def test_reset_reset_high(self):
        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 10
        reset_msg.Header.MsgSeqNum = 999
        reset_msg.GapFillFlag = 'N'

        self.client_app.send_message(self._testMethodName, reset_msg)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 10

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(self.client_app)

    """Receive Sequence Reset (Reset)<4> message with NewSeqNo(36) = to expected sequence number	
    Accept the Sequence Reset (Reset) message without regards to its MsgSeqNum(34)
    Generate a "warning" condition in test output"""

    def test_reset_reset_same(self):
        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 3
        reset_msg.GapFillFlag = 'N'
        reset_msg.Header.MsgSeqNum = 999

        self.client_app.send_message(self._testMethodName, reset_msg)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 3

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.SequenceReset)

        self.do_logout(self.client_app)

    """Receive Sequence Reset (Reset)<4> message with NewSeqNo(36) < than expected sequence number	
    Accept the Sequence Reset (Reset) message without regards to its MsgSeqNum(34)
    Send Reject<3> (session-level) message referencing invalid MsgType(35) (≥ FIX 4.2: SessionRejectReason(373) = 5 - "Value is incorrect (out of range) for this tag")
    Do NOT Increment inbound MsgSeqNum
    Generate an "error" condition in test output
    Do NOT lower expected sequence number"""

    def test_reset_reset_low(self):
        reset_msg = fix_messages_4_2_0_base.SequenceReset()
        reset_msg.NewSeqNo = 0
        reset_msg.GapFillFlag = 'N'

        self.client_app.send_message(self._testMethodName, reset_msg)
        self.client_app.engines[self._testMethodName].msg_seq_num_out = 3

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXResetSequenceToLowerError)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

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
