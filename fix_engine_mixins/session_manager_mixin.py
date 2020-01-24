import logging
import asyncio
import fix_engine
import heapq
import fix_errors
import datetime
import fix_message
import datetime
import concurrent

logger = logging.getLogger(__name__)

class SessionManagerInitiatorMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logon_time = None
        self.logout_time = None
        self.is_reconnect = False
        self.logon_handle = None
        self.logout_handle = None

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.logon_time = datetime.datetime.strptime(self.settings.get('LogonTime'), '%H:%M:%S').time()
        self.logout_time = datetime.datetime.strptime(self.settings.get('LogoutTime'), '%H:%M:%S').time()
        self.check_new_day()

    def reconnect(self):
        self.store = self.store_factory.create_storage(self.settings)
        self.application._on_reconnect(self.session_name)
        self.check_new_day()

    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        if self.logout_handle: self.logout_handle.cancel()
        if self.logon_handle: self.logon_handle.cancel()

    def check_new_day(self):
        session_time = datetime.datetime.fromtimestamp(self.store.get_session_time())
        next_logout = self.calc_next_time(session_time, self.logout_time, datetime.timedelta(days=0))
        if next_logout < 0:
            self.store.new_day()

    async def start(self):
        if self.is_reconnect:
            self.reconnect()

        logon_offset = datetime.timedelta(days=0)
        logout_offset = datetime.timedelta(days=0)

        current_time = datetime.datetime.utcnow()
        next_logon = self.calc_next_time(current_time, self.logon_time, logon_offset)
        next_logout = self.calc_next_time(current_time, self.logout_time, logout_offset)

        self.logon_handle = self.loop.call_later(next_logon, self.handle_logon_timer)
        self.logout_handle = self.loop.call_later(next_logout, self.handle_logout_timer)

        try:
            await self.serve_client()
            self.writer.close()
            await self.writer.wait_closed()
        except concurrent.futures.CancelledError:
            pass
        except ConnectionResetError:
            logger.error("Server Closed Connection")
        except:
            logger.exception("Error in client")

        self.is_reconnect = True

    def inside_time_range(self, start, end):
        current_time = datetime.datetime.utcnow()
        start_time = datetime.datetime.combine(current_time, start)
        end_time = datetime.datetime.combine(current_time, end)

        if start_time <= end_time:
            #1 second grace period in case timer fires early
            if (current_time - start_time) > datetime.timedelta(seconds = -1) and (current_time - end_time) < datetime.timedelta(seconds = 1) :
                return True
        else:
            if (current_time - start_time) > datetime.timedelta(seconds = -1) or (current_time - end_time) < datetime.timedelta(seconds = 1):
                return True
        return False

    def handle_logon_timer(self):
        if self.inside_time_range(self.logon_time, self.logout_time):
            self.send_logon()
        offset = datetime.timedelta(days=1)
        next = self.calc_next_time(datetime.datetime.utcnow(), self.logon_time, offset)
        logger.debug(f"Next Logon scheduled in {next} seconds")
        self.logon_handle = self.loop.call_later(next, self.handle_logon_timer)

    def handle_logout_timer(self):
        if self.inside_time_range(self.logout_time, self.logon_time):
            self.logout()
        else:
            logger.debug("Logout timer called when not inside range")
        offset = datetime.timedelta(days=1)
        next = self.calc_next_time(datetime.datetime.utcnow(), self.logout_time, offset)
        logger.debug(f"Next Logout scheduled in {next} seconds")
        self.logout_handle = self.loop.call_later(next, self.handle_logout_timer)

    def calc_next_time(self, from_date_time, time, offset):
        next = datetime.datetime.combine(from_date_time + offset, time)
        now = datetime.datetime.utcnow()

        delta = next - now
        return delta.total_seconds()


class SessionManagerAcceptorMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logon_time = None
        self.logout_time = None
        self.logout_handle = None

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.logon_time = datetime.datetime.strptime(self.settings.get('LogonTime'), '%H:%M:%S').time()
        self.logout_time = datetime.datetime.strptime(self.settings.get('LogoutTime'), '%H:%M:%S').time()

        logout_offset = datetime.timedelta(days=0)

        current_time = datetime.datetime.utcnow()
        next_logout = self.calc_next_time(current_time, self.logout_time, logout_offset)

        self.logout_handle = self.loop.call_later(next_logout, self.handle_logout_timer)

        self.check_new_day()

    def register_admin_messages(self, *args, **kwargs):
        self.register_admin_callback(self.message_lib.fix_messages.Logon, self.on_logon_check_time, 
            priority = fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.HIGH + 2*fix_engine.CallbackRegistrar.CALLBACK_PRIORITY.BEFORE)
        super().register_admin_messages(*args, **kwargs)

    def on_logon_check_time(self, session_name, msg):
        if not self.inside_time_range(self.logon_time, self.logout_time):
            error = "Application not available"
            self.application._on_error(self.session_name, fix_errors.FIXUnsupportedMessageTypeError(msg.Header.MsgSeqNum, msg._msgtype, None, error, self.message_lib.fields.BusinessRejectReason.ENUM_UNSUPPORTED_MESSAGE_TYPE))
            self.send_biz_reject(msg.Header.MsgSeqNum, msg._msgtype, None, error, self.message_lib.fields.BusinessRejectReason.ENUM_APPLICATION_NOT_AVAILABLE)
            raise fix_errors.FIXDropMessageError("Application not available")


    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        if self.logout_handle: self.logout_handle.cancel()

    def check_new_day(self):
        session_time = datetime.datetime.fromtimestamp(self.store.get_session_time())
        next_logout = self.calc_next_time(session_time, self.logout_time, datetime.timedelta(days=0))
        if next_logout < 0:
            logger.debug("Performing New Day on session")
            self.store.new_day()

    async def start(self):
        try:
            await self.serve_client()
            self.writer.close()
            await self.writer.wait_closed()
        except concurrent.futures._base.CancelledError:
            pass

    def inside_time_range(self, start, end):
        current_time = datetime.datetime.utcnow()
        start_time = datetime.datetime.combine(current_time, start)
        end_time = datetime.datetime.combine(current_time, end)

        if start_time <= end_time:
            #1 second grace period in case timer fires early
            if (current_time - start_time) > datetime.timedelta(seconds = -1) and (current_time - end_time) < datetime.timedelta(seconds = 1) :
                return True
        else:
            if (current_time - start_time) > datetime.timedelta(seconds = -1) or (current_time - end_time) < datetime.timedelta(seconds = 1):
                return True
        return False

    def handle_logout_timer(self):
        if self.inside_time_range(self.logout_time, self.logon_time):
            self.logout()
        else:
            logger.debug("Logout timer called when not inside range")
        offset = datetime.timedelta(days=1)
        next = self.calc_next_time(datetime.datetime.utcnow(), self.logout_time, offset)
        logger.debug(f"Next Logout scheduled in {next} seconds")
        self.logout_handle = self.loop.call_later(next, self.handle_logout_timer)

    def calc_next_time(self, from_date_time, time, offset):
        next = datetime.datetime.combine(from_date_time + offset, time)
        now = datetime.datetime.utcnow()

        delta = next - now
        return delta.total_seconds()




