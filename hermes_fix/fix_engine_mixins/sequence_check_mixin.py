import logging

from .. import fix_engine, fix_errors, fix_message, fix_message_library
from ..fix_callbacks import CallbackRegistrar
from ..utils.log import logger


class SequenceCheckerMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(
            None, self.on_msg_check_seq, CallbackRegistrar.CALLBACK_PRIORITY.HIGH)
        self.register_admin_callback(self.message_lib.fix_messages.SequenceReset,
                                     self.on_sequence_reset, CallbackRegistrar.CALLBACK_PRIORITY.NORMAL)
        self.register_admin_callback(
            self.message_lib.fix_messages.ResendRequest, self.on_resend_request)

    def on_sequence_reset(self, session_name, msg):
        in_seq = self.store.get_current_in_seq()
        force_seq = msg.NewSeqNo-1

        # don't check sequences if they are being hard reset
        if msg.GapFillFlag != self.message_lib.fields.GapFillFlag.ENUM_GAP_FILL_MESSAGE and msg.NewSeqNo >= in_seq:
            logger.warning(
                f"Updating Seq number and Dropping processing of SequenceReset because its a non-GapFill reset")
            self.store.set_current_in_seq(force_seq)
            return

        if in_seq >= msg.NewSeqNo:
            '''Send Reject<3> (session-level) message with message "attempt to lower sequnce number, invalid value NewSeqNum=<x>"'''
            raise fix_errors.FIXResetSequenceToLowerError(msg.Header.MsgSeqNum, msg._msgtype, msg.tags.NewSeqNo,
                                                          f"attempt to lower sequnce number, invalid value NewSeqNum={msg.NewSeqNo}", self.message_lib.fields.SessionRejectReason.ENUM_VALUE_IS_INCORRECT)

        if msg.Header.MsgSeqNum != in_seq:  # discard sequence reset if numbers don't match but process for potential resend request
            return

        self.store.set_current_in_seq(force_seq)

    def on_msg_check_seq(self, session_name, msg):

        if isinstance(msg, self.message_lib.fix_messages.SequenceReset) and msg.GapFillFlag != self.message_lib.fields.GapFillFlag.ENUM_GAP_FILL_MESSAGE:
            # SequenceReset - Reset: ignore all sequence checks
            return

        in_seq = self.store.get_current_in_seq()+1
        if msg.Header.MsgSeqNum == in_seq:
            self.check_seq_same(msg)
            self.store.set_current_in_seq(msg.Header.MsgSeqNum)
        elif msg.Header.MsgSeqNum > in_seq:
            logger.warning(
                f"Expected incoming sequence [{in_seq}] but received [{msg.Header.MsgSeqNum}]")
            if self.waiting_for_logout:
                return
            self.do_resend_request(in_seq)
            if msg._msgcat != 'admin':  # since admin messages do not get resent we'll let this one through but will not update seq num
                raise fix_errors.FIXEngineResendRequest("Resend Requested")
            else:
                self.application._on_error(
                    self.session_name, fix_errors.FIXEngineResendRequest("Resend Requested"))
            return
        elif msg.Header.MsgSeqNum < in_seq:
            self.check_low_seq(in_seq, msg)

    def do_resend_request(self, in_seq):
        resend_request = self.message_lib.fix_messages.ResendRequest()
        resend_request.BeginSeqNo = in_seq
        resend_request.EndSeqNo = 0
        self.send_message(resend_request)

    def check_low_seq(self, in_seq, msg):
        if msg.Header.PossDupFlag != self.message_lib.fields.PossDupFlag.ENUM_POSSIBLE_DUPLICATE:
            error = f"Incoming message sequence too low expected [{in_seq}] but received [{msg.Header.MsgSeqNum}]"
            raise fix_errors.FIXSequenceTooLowError(error)
        if msg.Header.PossDupFlag == self.message_lib.fields.PossDupFlag.ENUM_POSSIBLE_DUPLICATE and msg.Header.OrigSendingTime <= msg.Header.SendingTime:
            logger.debug("Discarding dupe message")
            raise fix_errors.FIXDupeMessageRecv(
                "Duplicate message received, discarding")
        else:
            logger.warning(
                "Accepting message with PossDupe=Y and lower sequence number")

    def check_seq_same(self, msg):
        if msg.Header.PossDupFlag == self.message_lib.fields.PossDupFlag.ENUM_POSSIBLE_DUPLICATE and msg.Header.OrigSendingTime > msg.Header.SendingTime:
            raise fix_errors.FIXSendTimeAccuracyError(msg.Header.MsgSeqNum, msg._msgtype, msg.Header.tags.OrigSendingTime,
                                                      "SendingTime accuracy problem", self.message_lib.fields.SessionRejectReason.ENUM_SENDING_TIME_ACCURACY_PROBLEM)

    def send_gap_fill(self, last_sent_msg_num, msg_num):
        gap_msg = self.message_lib.fix_messages.SequenceReset()
        gap_msg.GapFillFlag = self.message_lib.fields.GapFillFlag.ENUM_GAP_FILL_MESSAGE
        gap_msg.NewSeqNo = msg_num
        gap_msg.Header.MsgSeqNum = last_sent_msg_num+1
        self.send_message(gap_msg, resend=True)

    def on_resend_request(self, session_name, msg):
        last_sent_msg_num = msg.BeginSeqNo-1
        for msg_num, msg_type_str, resend_msg in self.store.get_messages(msg.BeginSeqNo, msg.EndSeqNo):
            try:
                msg = fix_message_library.create_message_from_binary(
                    resend_msg, msg_type_str, self.message_lib)
            except Exception:
                logger.exception("Failed to replay message")
                self.send_gap_fill(last_sent_msg_num, msg_num+1)
                last_sent_msg_num = msg_num
                continue

            if msg._msgcat == 'app' or isinstance(msg, self.message_lib.fix_messages.Logout):
                if last_sent_msg_num < msg_num-1:
                    self.send_gap_fill(last_sent_msg_num, msg_num)
                self.send_message(msg, resend=True)
                last_sent_msg_num = msg_num

        if last_sent_msg_num < self.msg_seq_num_out-1:
            self.send_gap_fill(last_sent_msg_num, self.msg_seq_num_out)
