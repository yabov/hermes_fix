import unittest 
import asyncio

import fix_errors
import fix
import message_lib.FIX_4_2.fix_messages as fix_messages_4_2_0_base
import logging
import queue
import datetime
import fix_message
import io
import os

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

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.TestRequest)
        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)
        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Heartbeat)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Logout)

    def build_raw_msg(self, body):
        raw_msg = io.BytesIO()        
        raw_msg.write(b'8=FIX.4.2\x01')
        raw_msg.write(f'9={len(body)}\x01'.encode())
        raw_msg.write(body)
        checksum = fix_message.calc_checksum(raw_msg)        
        raw_msg.write((f'10={checksum}\x01').encode())
        return raw_msg.getbuffer()

    """Receive field identifier (tag number) not defined in specification.
    Send Reject<3> (session-level) message referencing invalid tag number (≥ FIX 4.2: SessionRejectReason(373) = 0 - "Invalid tag number")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""
    def test_bad_field_no_validate(self):
        self.server_app.engine.accept_unknown_fields = True

        time = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|999=123|21=1|55=AAPL|54=1|60={time}|'.replace('|','\x01').encode()

        self.client_app.engine.writer.write(self.build_raw_msg(body))
        self.client_app.engine.msg_seq_num_out +=1

        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.OrderSingle)

        self.do_logout(self.client_app)


    def test_bad_field_validate(self):

        time = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|999=123|21=1|55=AAPL|54=1|60={time}|'.replace('|','\x01').encode()

        self.client_app.engine.writer.write(self.build_raw_msg(body))
        self.client_app.engine.msg_seq_num_out +=1


        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ Receive message with a required field identifier (tag number) missing.	
    Send Reject (session-level) message referencing required tag missing (≥ FIX 4.2: SessionRejectReason(373) = 1 - "Required tag missing")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""
    def test_missing_req_field(self):

        time = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|21=1|54=1|60={time}|'.replace('|','\x01').encode()

        self.client_app.engine.writer.write(self.build_raw_msg(body))
        self.client_app.engine.msg_seq_num_out +=1


        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXInvalidMessageFieldError)

        self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """ Receive message with field identifier (tag number) specified but no value (e.g. "55=<SOH>" vs. "55=IBM<SOH>").	

    TODO Needs option for below:
    Send Reject<3> (session-level) message referencing tag not defined for this message type (≥ FIX 4.2: SessionRejectReason(373) = 4 - "Tag specified without a value")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""
    def test_missing_field_value(self):

        time = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=1|21=1|1=|55=AAPL|54=1|60={time}|'.replace('|','\x01').encode()

        self.client_app.engine.writer.write(self.build_raw_msg(body))
        self.client_app.engine.msg_seq_num_out +=1


        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_messages_4_2_0_base.OrderSingle)

        #self.assertIsInstance(CLIENT_QUEUE.get(timeout=2), fix_messages_4_2_0_base.Reject)

        self.do_logout(self.client_app)

    """Receive message with incorrect value (out of range or not part of valid list of enumerated values) for a particular field identifier (tag number).
    Exception: undefined enumeration values used are specified in testing profile as user-defined.	
    Send Reject<3> (session-level) message referencing tag not defined for this message type (≥ FIX 4.2: SessionRejectReason(373) = 5 - "Value is incorrect (out of range) for this tag")
    Increment inbound MsgSeqNum(34)
    Generate an "error" condition in test output"""
    def test_value_out_of_range(self):

        time = datetime.datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')
        body = f'35=D|49={self._testMethodName}|56=HOST|34=2|52={time}|11=test_message|40=999|21=1|55=AAPL|54=1|60={time}|'.replace('|','\x01').encode()

        self.client_app.engine.writer.write(self.build_raw_msg(body))
        self.client_app.engine.msg_seq_num_out +=1


        self.assertIsInstance(SERVER_QUEUE.get(timeout=2), fix_errors.FIXInvalidMessageFieldError)

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
