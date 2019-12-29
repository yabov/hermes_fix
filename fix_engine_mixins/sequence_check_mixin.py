import logging
import fix_message_library
import fix_engine
import fix_message
import fix_errors

logger = logging.getLogger(__name__)

class SequenceCheckerMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_callback(None, self.on_msg_check_seq, fix_engine.CallbackWrapper.CALLBACK_PRIORITY.HIGH)
        self.register_callback(self.message_lib.SequenceReset, self.on_sequence_reset, fix_engine.CallbackWrapper.CALLBACK_PRIORITY.HIGH+1)
        self.register_callback(self.message_lib.ResendRequest, self.on_resend_request)

    def on_sequence_reset(self, msg):
        in_seq = self.store.get_current_in_seq()+1
        force_seq = None
        if in_seq > msg.NewSeqNo:
            raise fix_errors.FIXSequenceTooLowError(f"Expected incoming sequence [{in_seq}] but received [{msg.NewSeqNo}]")
        force_seq = msg.NewSeqNo-1
        self.store.set_current_in_seq(force_seq)
        #if msg.GapFillFlag != self.message_lib.GapFillFlag.ENUM_YES:
        #    raise FIXIngoreSequenceCheck("Not a GapFill reset")
        

    def on_msg_check_seq(self, msg):
        in_seq = self.store.get_current_in_seq()+1
        
        if self.check_poss_dupe_sendtime(in_seq, msg):
            pass
        elif msg.Header.MsgSeqNum == in_seq:
            self.check_seq_same(msg)
        elif msg.Header.MsgSeqNum > in_seq:
            logger.warning(f"Expected incoming sequence [{in_seq}] but received [{msg.Header.MsgSeqNum}]")
            self.do_resend_request(in_seq)
        elif msg.Header.MsgSeqNum < in_seq:
            self.check_low_seq(in_seq, msg)
            
        #self.store.set_current_in_seq(in_seq)

    def check_poss_dupe_sendtime(self, in_seq, msg):
        if msg.Header.PossDupFlag == self.message_lib.PossDupFlag.ENUM_YES and msg.Header.OrigSendingTime is None:
            reject_msg = self.message_lib.Reject()
            try:
                reject_msg.RefSeqNum = msg.Header.MsgSeqNum
                reject_msg.RefMsgType = msg._msgtype
                reject_msg.RefTagID = msg.Header.OrigSendingTime._tag
                reject_msg.Text = "Required tag missing"
                reject_msg.SessionRejectReason = self.message_lib.SessionRejectReason.ENUM_REQUIRED_TAG_MISSING
            except:
                logger.exception("FAIL")
            self.send_message(reject_msg)
            self.store.set_current_in_seq(in_seq)
            raise fix_errors.RequiredTagMissingError("Required tag missing")
        return False

    def do_resend_request(self, in_seq):
        resend_request = self.message_lib.ResendRequest()
        resend_request.BeginSeqNo = in_seq
        resend_request.EndSeqNo = 0
        self.send_message(resend_request)
        raise fix_errors.FIXEngineResendRequest("Resend Requested")

    def check_low_seq(self, in_seq, msg):
        if msg.Header.PossDupFlag != self.message_lib.PossDupFlag.ENUM_YES:
            if isinstance(msg, self.message_lib.SequenceReset):
                return
            error = f"Incoming message sequence too low expected [{in_seq}] but received [{msg.Header.MsgSeqNum}]"
            raise fix_errors.FIXSequenceTooLowError (error)
        if msg.Header.PossDupFlag == self.message_lib.PossDupFlag.ENUM_YES and msg.Header.OrigSendingTime <= msg.Header.SendingTime:
            logger.debug("Discarding dupe message")
            raise fix_errors.FIXDupeMessageRecv("Duplicate message received, discarding")

    def check_seq_same(self, msg):
        self.store.set_current_in_seq(msg.Header.MsgSeqNum)
        if msg.Header.PossDupFlag == self.message_lib.PossDupFlag.ENUM_YES and msg.Header.OrigSendingTime > msg.Header.SendingTime:
            reject_msg = self.message_lib.Reject()
            try:
                reject_msg.RefSeqNum = msg.Header.MsgSeqNum
                reject_msg.RefMsgType = msg._msgtype
                reject_msg.RefTagID = msg.Header.tags.OrigSendingTime
                reject_msg.Text = "SendingTime accuracy problem"                
                reject_msg.SessionRejectReason = self.message_lib.SessionRejectReason.ENUM_SENDINGTIME_ACCURACY_PROBLEM
            except:
                pass
            self.send_message(reject_msg)
            raise fix_errors.FIXSendTimeAccuracyError("SendingTime accuracy problem")
            
    def send_gap_fill(self, last_sent_msg_num, msg_num):
        gap_msg = self.message_lib.SequenceReset()
        gap_msg.GapFillFlag = self.message_lib.GapFillFlag.ENUM_YES
        gap_msg.NewSeqNo = msg_num
        self.send_message(gap_msg, last_sent_msg_num)

    def on_resend_request(self, msg):
        last_sent_msg_num = msg.BeginSeqNo-1
        for msg_num, msg_type_str, resend_msg in self.store.get_messages(msg.BeginSeqNo, msg.EndSeqNo):
            try:
                msg = fix_message_library.create_message_from_binary(resend_msg, msg_type_str, self.message_lib)
            except:
                self.send_gap_fill(last_sent_msg_num+1, msg_num+1)
                last_sent_msg_num = msg_num
                continue
            msg.Header.PossDupFlag = 'Y'
            msg.Header.OrigSendingTime = msg.Header.SendingTime
            if msg._msgcat == 'app' or isinstance(msg, self.message_lib.Logout):
                if last_sent_msg_num < msg_num-1:
                    self.send_gap_fill(last_sent_msg_num+1, msg_num)
                self.send_message(msg, msg_num)
                last_sent_msg_num = msg_num
        
        if last_sent_msg_num < self.msg_seq_num_out-1:
            self.send_gap_fill(last_sent_msg_num+1, self.msg_seq_num_out)