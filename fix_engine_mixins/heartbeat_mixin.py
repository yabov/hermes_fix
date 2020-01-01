import logging
import asyncio
import threading
import fix_engine

logger = logging.getLogger(__name__)

class HeartBeatMixin: 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.out_heart_beat_int = None
        self.out_heart_beat_task = None
        self.in_heart_beat_int = None
        self.in_heart_beat_task = None

        self.hearbeat_grace_period = 1.2 #20% more than heartbeat

        self.waiting_for_test_msg_id = None
        self.heart_beat_loop = None

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.out_heart_beat_int = float(self.settings.get('HeartBeatInt', '30'))

    def register_admin_messages(self, *args, **kwargs):
        super().register_admin_messages(*args, **kwargs)
        self.register_admin_callback(self.message_lib.Logon, self.on_logon_hb)
        self.register_admin_callback(self.message_lib.Heartbeat, self.on_heart_beat)
        self.register_admin_callback(self.message_lib.TestRequest, self.on_test_request)
        self.register_admin_callback(None, self.on_any_msg, priority = fix_engine.CallbackWrapper.CALLBACK_PRIORITY.LAST)

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
        if not self.waiting_for_test_msg_id:
            future = asyncio.run_coroutine_threadsafe(self.schedule_next_in_beat_await(), self.loop)
            future.result()


    def on_logon_hb(self, msg):
        self.in_heart_beat_int = msg.HeartBtInt
        self.register_heartbeats()

    #async def schedule_next_beat(self):
    #    self.loop.call_later(self.out_heart_beat_int, self.out_heart_beat)

    async def schedule_next_out_beat_await(self):
        self.schedule_next_out_beat()

    def schedule_next_out_beat(self):
        if self.out_heart_beat_task:
            self.out_heart_beat_task.cancel()

        logger.debug (self.out_heart_beat_int)
        self.out_heart_beat_task = self.loop.call_later(self.out_heart_beat_int, self.out_heart_beat)

    async def schedule_next_in_beat_await(self):
        self.schedule_next_in_beat()

    def schedule_next_in_beat(self):
        if self.in_heart_beat_task:
            self.in_heart_beat_task.cancel()
        self.in_heart_beat_task = self.loop.call_later(self.in_heart_beat_int*self.hearbeat_grace_period, self.in_heart_beat)


    def register_heartbeats(self):
        logger.debug("Registering Heartbeats")    
        
        future_out = asyncio.run_coroutine_threadsafe(self.schedule_next_out_beat_await(), self.loop)
        future_in = asyncio.run_coroutine_threadsafe(self.schedule_next_in_beat_await(), self.loop)
        future_out.result()
        future_in.result()

        #self.out_heart_beat_task =  self.loop.call_soon_threadsafe(self.out_heart_beat())
        #self.in_heart_beat_task = self.loop.create_task(self.in_heart_beat())

    """async def out_heart_beat(self):
        while self.is_logged_on():
            await asyncio.sleep(self.out_heart_beat_int)
            hrtbt= self.message_lib.Heartbeat()
            self.send_message(hrtbt)"""

    def out_heart_beat(self):
        hrtbt= self.message_lib.Heartbeat()
        self.send_message(hrtbt)   
        self.schedule_next_out_beat()

    def on_test_request(self, msg):
        hrtbt= self.message_lib.Heartbeat()
        hrtbt.TestReqID = msg.TestReqID
        return hrtbt

    def in_heart_beat(self):
        logger.warning("Missed heartbeat")
        if self.waiting_for_test_msg_id:
            self.no_heart_beat()
        self.send_test_message()
        self.schedule_next_in_beat()

    def send_test_message(self):
        msg = self.message_lib.TestRequest()
        msg.TestReqID = self.msg_seq_num_out
        self.waiting_for_test_msg_id = self.msg_seq_num_out
        self.send_message(msg)

    def no_heart_beat(self):
        logger.error("Failed to respond to TestRequest, closing")
        self.logout()

    def on_heart_beat(self, msg):
        print ("before")
        if self.waiting_for_test_msg_id:
            if msg.TestReqID == self.waiting_for_test_msg_id:
                self.waiting_for_test_msg_id = None
        future = asyncio.run_coroutine_threadsafe(self.schedule_next_in_beat_await(), self.loop)
        future.result()
        print ("On beat")

    def _send(self, *args, **kwargs):
        super()._send(*args, **kwargs)
        if self.out_heart_beat_task:
            self.schedule_next_out_beat()
            
