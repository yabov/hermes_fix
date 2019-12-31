import logging
import asyncio
import threading

logger = logging.getLogger(__name__)

class HeartBeatMixin: 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.out_heart_beat_int = None
        self.out_heart_beat_task = None
        self.in_heart_beat_int = None
        self.in_heart_beat_task = None

        self.hearbeat_grace_period = 15 #seconds to wait for heartbeat grace period

        self.heart_beat_received = None
        self.waiting_for_test_msg_id = None
        self.heart_beat_loop = None

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.out_heart_beat_int = float(self.settings.get('HeartBeatInt', '30'))

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(self.message_lib.Logon, self.on_logon_hb)
        self.register_admin_callback(self.message_lib.Heartbeat, self.on_heart_beat)
        self.register_admin_callback(None, self.on_any_msg)

    def build_logon_msg(self, *args, **kwargs):
        msg = super().build_logon_msg(*args, **kwargs)
        msg.HeartBtInt = self.out_heart_beat_int

        return msg

    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        try:
            if self.heart_beat_loop:
                self.out_heart_beat_task.cancel()
                self.in_heart_beat_task.cancel()
                self.heart_beat_loop.stop()
        except:
            logger.exception("Failed to close heartbeats")

    def on_any_msg(self, msg):
        self.heart_beat_received = True #heartbeat or not we received a message

    def on_logon_hb(self, msg):
        self.in_heart_beat_int = msg.HeartBtInt
        self.register_heartbeats()

    async def schedule_next_beat(self):
        self.loop.call_later(self.out_heart_beat_int, self.out_heart_beat)

    def register_heartbeats(self):
        logger.debug("Registering Heartbeats")    
        
        self.out_heart_beat_task = asyncio.run_coroutine_threadsafe(self.schedule_next_beat(), self.loop)
        #self.in_heart_beat_task = asyncio.run_coroutine_threadsafe(self.in_heart_beat(), self.heart_beat_loop)

        #self.out_heart_beat_task =  self.loop.create_task(self.out_heart_beat())
        #self.in_heart_beat_task = self.loop.create_task(self.in_heart_beat())

    """async def out_heart_beat(self):
        while self.is_logged_on():
            await asyncio.sleep(self.out_heart_beat_int)
            hrtbt= self.message_lib.Heartbeat()
            self.send_message(hrtbt)"""
    def out_heart_beat(self):
        hrtbt= self.message_lib.Heartbeat()
        self.send_message(hrtbt)   
        self.out_heart_beat_task = asyncio.run_coroutine_threadsafe(self.schedule_next_beat(), self.loop)

    async def in_heart_beat(self):
        while self.is_logged_on():
            await asyncio.sleep(self.out_heart_beat_int+ self.hearbeat_grace_period)
            if self.waiting_for_test_msg_id:
                await self.no_heart_beat()
            elif not self.heart_beat_received:
                logger.warning("Missed heartbeat")
                self.send_test_message()

    def send_test_message(self):
        msg = self.message_lib.TestRequest()
        msg.TestReqID = self.msg_seq_num_out
        self.waiting_for_test_msg_id = self.msg_seq_num_out
        self.send_message(msg)

    async def no_heart_beat(self):
        logger.error("Failed to respond to TestRequest, closing")
        self.logout()

    def on_heart_beat(self, msg):
        if self.waiting_for_test_msg_id:
            if msg.TestReqID == self.waiting_for_test_msg_id:
                self.waiting_for_test_msg_id = None