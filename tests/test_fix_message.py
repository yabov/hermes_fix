import unittest
import asyncio

import logging
import queue
from datetime import datetime, timedelta
import io
import os

from hermes_fix import fix_errors
from hermes_fix import fix
from hermes_fix import fix_engine
from hermes_fix.message_lib.FIX_4_2 import fix_messages as fix_messages_4_2_0_base
from hermes_fix import fix_message


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

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Logout)

    def build_raw_msg(self, body):
        raw_msg = io.BytesIO()
        raw_msg.write(b'8=FIX.4.2\x01')
        raw_msg.write(f'9={len(body)}\x01'.encode())
        raw_msg.write(body)
        checksum = fix_message.calc_checksum(raw_msg)
        raw_msg.write((f'10={checksum}\x01').encode())
        return raw_msg.getbuffer()

    """Message with repeating group"""

    def test_group_msg(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.NoAllocs = 2
        ord_allocs1 = fix_messages_4_2_0_base.NoAllocsGroup()
        ord_allocs1.AllocAccount = 'Abc'
        ord_allocs1.AllocShares = 123
        ord_allocs2 = fix_messages_4_2_0_base.NoAllocsGroup()
        ord_allocs2.AllocAccount = 'Def'
        ord_allocs2.AllocShares = 456
        order_msg.NoAllocsGroup = [ord_allocs1, ord_allocs2]

        self.client_app.send_message(self._testMethodName, order_msg)

        msg = SERVER_QUEUE.get(timeout=3)
        self.assertIsInstance(msg, fix_messages_4_2_0_base.OrderSingle)
        self.assertEqual(msg.NoAllocs, 2)
        self.assertEqual(msg.NoAllocsGroup[0].AllocAccount, 'Abc')
        self.assertEqual(msg.NoAllocsGroup[0].AllocShares, 123)
        self.assertEqual(msg.NoAllocsGroup[1].AllocAccount, 'Def')
        self.assertEqual(msg.NoAllocsGroup[1].AllocShares, 456)

        self.do_logout(self.client_app)

    """Receive field identifier (tag number) not defined in specification.
    Send Reject<3> (session-level) message referencing invalid tag number (≥ FIX 4.2: SessionRejectReason(373) = 0 - "Invalid tag number")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_bad_field_no_validate(self):
        self.server_app.engines[self._testMethodName].accept_unknown_fields = True

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|999=123|21=1|55=AAPL|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.OrderSingle)

        self.do_logout(self.client_app)

    def test_bad_field_validate(self):

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|999=123|21=1|55=AAPL|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ Receive message with a required field identifier (tag number) missing.	
    Send Reject (session-level) message referencing required tag missing (≥ FIX 4.2: SessionRejectReason(373) = 1 - "Required tag missing")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_missing_req_field(self):

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|21=1|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ Receive message with field identifier (tag number) specified but no value (e.g. "55=<SOH>" vs. "55=IBM<SOH>").	
    Send Reject<3> (session-level) message referencing tag not defined for this message type (≥ FIX 4.2: SessionRejectReason(373) = 4 - "Tag specified without a value")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_missing_field_value(self):

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|21=1|1=|55=AAPL|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """Receive message with incorrect value (out of range or not part of valid list of enumerated values) for a particular field identifier (tag number).
    Exception: undefined enumeration values used are specified in testing profile as user-defined.	
    Send Reject<3> (session-level) message referencing tag not defined for this message type (≥ FIX 4.2: SessionRejectReason(373) = 5 - "Value is incorrect (out of range) for this tag")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_value_out_of_range(self):

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=999|21=1|55=AAPL|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """Receive message with a value in an incorrect data format (syntax) for a particular field identifier (tag number).	
    Send Reject<3> (session-level) message referencing tag not defined for this message type (≥ FIX 4.2: SessionRejectReason(373) = 6 - "Incorrect data format for value")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_value_incorrect(self):

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|38=a|40=1|21=1|55=AAPL|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """Receive a message in which a field identifier (tag number) which is not part of a repeating group is specified more than once	
    Send Reject<3> (session-level) message referencing duplicate field identifier (tag number) (≥ FIX 4.3: SessionRejectReason(373) = 13 "Tag appears more than once")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_dupe_field_val(self):

        time = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|38=10|40=1|21=1|55=AAPL|11=test_message|54=1|60={time}|'.replace(
            '|', '\x01').encode()

        self.client_app.engines[self._testMethodName].writer.write(
            self.build_raw_msg(body))
        self.client_app.engines[self._testMethodName].msg_seq_num_out += 1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXRepeatingFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ Receive a message with repeating groups in which the "count" field value for a repeating group is incorrect	
    Send Reject<3> (session-level) message referencing the incorrect "count" field identifier (tag number) (≥ FIX 4.3: SessionRejectReason(373) = 16 - "Incorrect NumInGroup count for repeating group")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""

    def test_bad_repeating_count(self):
        order_msg = fix_messages_4_2_0_base.OrderSingle()
        order_msg.ClOrdID = "test_message"
        order_msg.HandlInst = '1'
        order_msg.Symbol = 'AAPL'
        order_msg.Side = '1'
        order_msg.OrdType = '1'
        order_msg.TransactTime = datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        order_msg.NoAllocs = 3
        ord_allocs1 = fix_messages_4_2_0_base.NoAllocsGroup()
        ord_allocs1.AllocAccount = 'Abc'
        ord_allocs1.AllocShares = 123
        ord_allocs2 = fix_messages_4_2_0_base.NoAllocsGroup()
        ord_allocs2.AllocAccount = 'Def'
        ord_allocs2.AllocShares = 456
        order_msg.NoAllocsGroup = [ord_allocs1, ord_allocs2]

        self.client_app.send_message(self._testMethodName, order_msg)

        self.assertIsInstance(SERVER_QUEUE.get(timeout=3),
                              fix_errors.FIXIncorrectNumInGroup)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=3),
                              fix_messages_4_2_0_base.Reject)

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
