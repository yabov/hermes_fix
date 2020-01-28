import asyncio
import concurrent
import datetime
import heapq
import logging

from .. import fix_engine, fix_errors, fix_message
from ..fix_callbacks import CallbackRegistrar
from ..utils.log import logger


class SessionManagerBaseMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logon_time = None
        self.logout_time = None
        self.is_reconnect = False
        self.logon_handle = None
        self.logout_handle = None

    def check_new_day(self):
        session_time = datetime.datetime.fromtimestamp(
            self.store.get_session_time())
        next_logout = self.calc_next_time(session_time, self.logout_time)
        if next_logout < 0:
            self.store.new_day()

    def handle_logout_timer(self):
        if self.inside_time_range(self.logout_time, self.logon_time) and self.is_logged_on():
            logger.debug("Logging out")
            self.logout()
        else:
            pass
            # logger.debug(
            #    f"Not inside logout window of {self.logon_time} to {self.logout_time}")

        next = self.calc_next_time(
            datetime.datetime.utcnow(), self.logout_time)
        logger.debug(f"Next Logout scheduled in {next} seconds")
        self.logout_handle = self.loop.call_later(
            next, self.handle_logout_timer)

    def calc_next_time(self, from_date_time, time):
        next = datetime.datetime.combine(from_date_time, time)
        now = datetime.datetime.utcnow()

        delta = next - now
        seconds = delta.total_seconds()
        one_day = 60*60*24
        if seconds < 0:
            return seconds + one_day
        else:
            return seconds

    def inside_time_range(self, start, end):
        current_time = datetime.datetime.utcnow()
        start_time = datetime.datetime.combine(current_time, start)
        end_time = datetime.datetime.combine(current_time, end)

        if start_time <= end_time:
            if (current_time > start_time) and (current_time < end_time):
                return True
        else:
            if (current_time > start_time) or (current_time < end_time):
                return True
        return False


class SessionManagerInitiatorMixin(SessionManagerBaseMixin):
    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.logon_time = datetime.datetime.strptime(
            self.settings.get('LogonTime'), '%H:%M:%S').time()
        self.logout_time = datetime.datetime.strptime(
            self.settings.get('LogoutTime'), '%H:%M:%S').time()
        logger.debug(
            f"Initiator {self.session_name} logon time: {self.logon_time}, logout time: {self.logout_time}")
        self.check_new_day()

    def reconnect(self):
        self.store = self.store_factory.create_storage(self.settings)
        self.application._on_reconnect(self.session_name)
        self.check_new_day()

    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        if self.logout_handle:
            self.logout_handle.cancel()
        if self.logon_handle:
            self.logon_handle.cancel()

    async def start(self):
        if self.is_reconnect:
            self.reconnect()

        self.handle_logon_timer()
        self.handle_logout_timer()

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

    def handle_logon_timer(self):
        if self.inside_time_range(self.logon_time, self.logout_time):
            logger.debug("Sending logon for initiator")
            self.send_logon()
        else:
            pass
            #logger.debug(f"Not inside logon window of {self.logon_time} to {self.logout_time}")
        next = self.calc_next_time(datetime.datetime.utcnow(), self.logon_time)
        logger.debug(f"Next Logon scheduled in {next} seconds")
        self.logon_handle = self.loop.call_later(next, self.handle_logon_timer)


class SessionManagerAcceptorMixin(SessionManagerBaseMixin):
    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.logon_time = datetime.datetime.strptime(
            self.settings.get('LogonTime'), '%H:%M:%S').time()
        self.logout_time = datetime.datetime.strptime(
            self.settings.get('LogoutTime'), '%H:%M:%S').time()
        logger.debug(
            f"Acceptor {self.session_name} logon time: {self.logon_time}, logout time: {self.logout_time}")

        self.handle_logout_timer()

        self.check_new_day()

    def register_admin_messages(self, *args, **kwargs):
        self.register_admin_callback(self.message_lib.fix_messages.Logon, self.on_logon_check_time,
                                     priority=CallbackRegistrar.CALLBACK_PRIORITY.HIGH + 2*CallbackRegistrar.CALLBACK_PRIORITY.BEFORE)
        super().register_admin_messages(*args, **kwargs)

    def on_logon_check_time(self, session_name, msg):
        if not self.inside_time_range(self.logon_time, self.logout_time):
            error = "Application not available"
            self.application._on_error(self.session_name, fix_errors.FIXUnsupportedMessageTypeError(
                msg.Header.MsgSeqNum, msg._msgtype, None, error, self.message_lib.fields.BusinessRejectReason.ENUM_UNSUPPORTED_MESSAGE_TYPE))
            self.send_biz_reject(msg.Header.MsgSeqNum, msg._msgtype, None, error,
                                 self.message_lib.fields.BusinessRejectReason.ENUM_APPLICATION_NOT_AVAILABLE)
            raise fix_errors.FIXDropMessageError("Application not available")

    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        if self.logout_handle:
            self.logout_handle.cancel()

    async def start(self):
        try:
            await self.serve_client()
            self.writer.close()
            await self.writer.wait_closed()
        except concurrent.futures._base.CancelledError:
            pass
