import asyncio
import logging
import threading

from .. import fix_engine
from ..fix_callbacks import CallbackRegistrar
from ..utils.log import logger


class HeartBeatMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.out_heart_beat_int = None
        self.out_heart_beat_task = None
        self.in_heart_beat_int = None
        self.in_heart_beat_task = None

        self.hearbeat_grace_period = 1.2  # 20% more than heartbeat

        self.waiting_for_test_msg_id = None

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.out_heart_beat_int = float(
            self.settings.get('HeartBeatInt', '30'))
        self.hearbeat_grace_period = float(
            self.settings.get('HeatBeatGracePeriod', '1.2'))

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(
            self.message_lib.fix_messages.Logon, self.on_logon_hb)
        self.register_admin_callback(
            self.message_lib.fix_messages.Heartbeat, self.on_heart_beat)
        self.register_admin_callback(
            self.message_lib.fix_messages.TestRequest, self.on_test_request)
        self.register_admin_callback(
            None, self.on_any_msg, priority=CallbackRegistrar.CALLBACK_PRIORITY.LAST)

    def build_logon_msg(self, *args, **kwargs):
        msg = super().build_logon_msg(*args, **kwargs)
        msg.HeartBtInt = self.out_heart_beat_int

        return msg

    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        if self.out_heart_beat_task:
            self.out_heart_beat_task.cancel()
        if self.in_heart_beat_task:
            self.in_heart_beat_task.cancel()

    def on_any_msg(self, session_name, msg):
        if not self.waiting_for_test_msg_id:
            future = asyncio.run_coroutine_threadsafe(
                self.schedule_next_in_beat_await(), self.loop)
            future.result()

    def on_logon_hb(self, session_name, msg):
        self.in_heart_beat_int = msg.HeartBtInt
        self.register_heartbeats()

    async def schedule_next_out_beat_await(self):
        self.schedule_next_out_beat()

    def schedule_next_out_beat(self):
        if self.out_heart_beat_task:
            self.out_heart_beat_task.cancel()

        self.out_heart_beat_task = self.loop.call_later(
            self.out_heart_beat_int, self.out_heart_beat)

    async def schedule_next_in_beat_await(self):
        self.schedule_next_in_beat()

    def schedule_next_in_beat(self):
        if not self.is_logged_on():
            return
        if self.in_heart_beat_task:
            self.in_heart_beat_task.cancel()
        self.in_heart_beat_task = self.loop.call_later(
            self.in_heart_beat_int*self.hearbeat_grace_period, self.in_heart_beat)

    def register_heartbeats(self):
        logger.debug("Registering Heartbeats")

        future_out = asyncio.run_coroutine_threadsafe(
            self.schedule_next_out_beat_await(), self.loop)
        future_out.result()

    def out_heart_beat(self):
        hrtbt = self.message_lib.fix_messages.Heartbeat()
        self.send_message(hrtbt)
        self.schedule_next_out_beat()

    def on_test_request(self, session_name, msg):
        hrtbt = self.message_lib.fix_messages.Heartbeat()
        hrtbt.TestReqID = msg.TestReqID
        return hrtbt

    def in_heart_beat(self):
        logger.warning("Missed heartbeat")
        if self.waiting_for_test_msg_id:
            self.no_heart_beat()
            return
        self.send_test_message()
        self.schedule_next_in_beat()

    def send_test_message(self):
        if self.waiting_for_test_msg_id:
            return  # do not send another TestRequest
        msg = self.message_lib.fix_messages.TestRequest()
        msg.TestReqID = self.msg_seq_num_out
        self.waiting_for_test_msg_id = self.msg_seq_num_out
        self.send_message(msg)

    def no_heart_beat(self):
        logger.error("Failed to respond to TestRequest")
        self.logout("Failed to respond to TestRequest",
                    wait_interval=2, send_test_msg=False)

    def on_heart_beat(self, session_name, msg):
        if self.waiting_for_test_msg_id:
            if msg.TestReqID == str(self.waiting_for_test_msg_id):
                self.waiting_for_test_msg_id = None

    def on_hb_logout(self, msg, text, wait_interval):
        super().logout(text, wait_interval)

    """It is recommended that before sending the Logout<5> message, a TestRequest<1> 
    should be issued to force a Heartbeat<0> from the other side. This helps to ensure that there are no sequence number gaps."""

    def logout(self, text=None, wait_interval=10, send_test_msg=True):
        if send_test_msg:
            curr_seq = str(self.msg_seq_num_out)
            self.register_admin_callback(self.message_lib.fix_messages.Heartbeat, lambda session_name, msg: self.on_hb_logout(msg, text, wait_interval),
                                         check_func=lambda msg: (
                                             msg.TestReqID == curr_seq),
                                         priority=CallbackRegistrar.CALLBACK_PRIORITY.HIGH,
                                         one_time=True, timeout=wait_interval, timeout_cb=self.no_heart_beat)
            self.send_test_message()
        else:
            super().logout(text, wait_interval)

    def _send(self, *args, **kwargs):
        super()._send(*args, **kwargs)
        if self.out_heart_beat_task:
            self.schedule_next_out_beat()
