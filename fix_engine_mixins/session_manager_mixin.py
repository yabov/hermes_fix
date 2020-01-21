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
        self.connection_start_time = None
        self.connection_end_time = None
        self.logon_time = None
        self.logout_time = None
        self.is_reconnect = False
        self.logon_handle = None
        self.logout_handle = None

    def init_settings(self, *args, **kwargs):
        super().init_settings(*args, **kwargs)
        self.logon_time = datetime.datetime.strptime(self.settings.get('LogonTime'), '%H:%M:%S').time()
        self.logout_time = datetime.datetime.strptime(self.settings.get('LogoutTime'), '%H:%M:%S').time()

    def reconnect(self):
        self.store = self.store_factory.create_storage(self.settings)
        self.application.on_reconnect(self.session_name)

    def close_connection(self, *args, **kwargs):
        super().close_connection(*args, **kwargs)
        if self.logout_handle: self.logout_handle.cancel()
        if self.logon_handle: self.logon_handle.cancel()

    async def start(self):
        if self.is_reconnect:
            self.reconnect()

        logon_offset = datetime.timedelta(days=0)
        logout_offset = datetime.timedelta(days=0)

        next_logon = self.calc_next_time(self.logon_time, logon_offset)
        next_logout = self.calc_next_time(self.logout_time, logout_offset)

        self.logon_handle = self.loop.call_later(next_logon, self.handle_logon_timer)
        self.logout_handle = self.loop.call_later(next_logout, self.handle_logout_timer)

        try:
            await self.serve_client()
            self.writer.close()
            await self.writer.wait_closed()
        except concurrent.futures._base.CancelledError:
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
        next = self.calc_next_time(self.logon_time, offset)
        logger.debug(f"Next Logon scheduled in {next} seconds")
        self.logon_handle = self.loop.call_later(next, self.handle_logon_timer)

    def handle_logout_timer(self):
        if self.inside_time_range(self.logout_time, self.logon_time):
            self.logout()
        else:
            logger.debug("Logout timer called when not inside range")
        offset = datetime.timedelta(days=1)
        next = self.calc_next_time(self.logout_time, offset)
        logger.debug(f"Next Logout scheduled in {next} seconds")
        self.logout_handle = self.loop.call_later(next, self.handle_logout_timer)

    def calc_next_time(self, time, offset):
        next = datetime.datetime.combine(datetime.datetime.utcnow() + offset, time)
        now = datetime.datetime.utcnow()

        delta = next - now
        return delta.total_seconds()




