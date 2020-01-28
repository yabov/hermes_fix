import asyncio
import concurrent
import configparser
import logging
import ssl
import threading
from datetime import datetime, timedelta
from threading import Thread

from .application import Application
from .file_store_factory import FileStoreFactory
from .fix_engine import FIXEngineAcceptor, FIXEngineInitiator
from .session_settings import SessionSettings
from .utils import constants
from .utils.log import logger


class SocketConnection:
    def __init__(self, application: Application, storeFactory: FileStoreFactory, settings: SessionSettings):
        self.settings = settings
        self.application = application
        self.storeFactory = storeFactory
        self.server_map = {}
        self.settings_map = {}
        self.session_settings = settings
        self.lock = None
        self.engine_tasks = None
        self.stop_called = False

    async def on_connected_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        sockname = writer.get_extra_info('sockname')
        logger.info(f'Accepted New Connection on [{sockname}]<-->[{addr}]')
        engine = FIXEngineAcceptor(
            self.application, self.storeFactory, self.session_settings, 'DEFAULT')
        engine.reader = reader
        engine.writer = writer

        try:
            await engine.start()
        except ConnectionResetError:
            logger.error("Client Closed Connection")
        except:
            logger.exception("Error in server")
        logger.info(f"Ending Connection on [{sockname}]<-->[{addr}]")

    def build_ssl_context(self, section):
        protocol = self.settings[section].get('SSLProtocol', None)
        if protocol is None:
            return None

        ssl_contex = ssl.SSLContext(
            getattr(ssl._SSLMethod, protocol))  # pylint: disable=no-member
        for option in self.settings[section].get('SSLOptions', '').split(','):
            ssl_contex.options |= getattr(ssl, option.strip())

        cert_file = self.settings[section].get('SSLCertFile', None)
        if cert_file:
            cert_key_file = self.settings[section].get('SSLCertKeyFile', None)
            cert_password = self.settings[section].get('SSLCertPassword', None)
            ssl_contex.load_cert_chain(
                cert_file, keyfile=cert_key_file, password=cert_password)

        ca_file = self.settings[section].get('SSLCAFile', None)
        ssl_contex.load_verify_locations(cafile=ca_file)

        ssl_contex.check_hostname = self.settings[section].getboolean(
            'SSLCheckHostName', None)

        verify_mode = self.settings[section].get('SSLVerifyMode', None)
        ssl_contex.verify_mode = getattr(
            ssl.VerifyMode, verify_mode)  # pylint: disable=no-member

        ciphers = self.settings[section].get('SSLCiphers', None)
        if ciphers:
            ssl_contex.set_ciphers(ciphers)

        return ssl_contex

    async def main(self, event_sync):
        engines = []
        self.lock = asyncio.Lock()
        for section in self.settings.sections():
            if self.settings[section]['ConnectionType'] == 'acceptor':
                self.application._on_created(section)
                engines.append(self.start_acceptor(section))
            elif self.settings[section]['ConnectionType'] == 'initiator':
                self.application._on_created(section)
                engines.append(self.start_initiator(section))

        self.engine_tasks = asyncio.gather(*engines)
        event_sync.set()
        try:
            await self.engine_tasks
        except concurrent.futures._base.CancelledError:
            pass
        except:
            logger.exception("engine ended with errors")

    async def start_acceptor(self, section):
        logger.debug(f"Starting Acceptor Session [{section}]...")
        ip = self.settings[section].get('SocketAcceptHost', 'localhost')
        port = self.settings[section]['SocketAcceptPort']
        server = None
        async with self.lock:
            if (ip, port) in self.server_map:
                logger.debug(f"Server already created on {ip}:{port}")
                server, _ = self.server_map[(ip, port)]
                self.settings_map[(self.settings[section]['SenderCompID'],
                                   self.settings[section]['TargetCompID'])] = self.settings[section]
                return
            else:
                logger.debug(f"Creating Acceptor on {ip}:{port}")
                try:
                    server = await asyncio.start_server(self.on_connected_client, ip, port)
                except:
                    logger.exception(f"Failed to start server on {ip}:{port}")
                self.server_map[(ip, port)] = (
                    server, asyncio.get_running_loop())

        addr = server.sockets[0].getsockname()
        logger.debug(f"Connection Created, serving on {addr}")

        async with server:
            try:
                await server.serve_forever()
            except asyncio.CancelledError:
                pass
        logger.debug("-----------------Ending Server-----------------")

    async def start_initiator(self, section):
        connection_start_time = datetime.strptime(
            self.settings[section].get('ConnectionStartTime'), '%H:%M:%S').time()
        connection_end_time = datetime.strptime(
            self.settings[section].get('ConnectionEndTime'), '%H:%M:%S').time()
        connection_retry = self.settings[section].get(
            "ConnectionRetryInterval", fallback=2)
        ip = self.settings[section].get(
            'SocketConnectHost', fallback='localhost')
        port = self.settings[section]['SocketConnectPort']

        engine = FIXEngineInitiator(
            self.application, self.storeFactory, self.session_settings, section)
        while not self.stop_called:
            reader, writer = await self.open_connection(ip, port, connection_retry, connection_start_time, connection_end_time)
            addr = writer.get_extra_info('peername')
            sockname = writer.get_extra_info('sockname')
            logger.info(f"Opened Connection on [{sockname}]<-->[{addr}]")
            engine.reader = reader
            engine.writer = writer
            try:
                await engine.start()
            except ConnectionResetError:
                logger.error("Server Closed Connection")
            except:
                logger.exception("Error in client")
            logger.info(f"Ending Connection on [{sockname}]<-->[{addr}]")
            if not self.stop_called:
                await asyncio.sleep(connection_retry)
                logger.info("Reconnection client...")

    def inside_time_range(self, start, end):
        current_time = datetime.utcnow().time()
        if start <= end:
            if current_time > start and current_time < end:
                return True
        else:
            if current_time > start or current_time < end:
                return True
        return False

    async def open_connection(self, ip, port, connection_retry, connection_start_time, connection_end_time):
        while not self.stop_called:
            if self.inside_time_range(connection_start_time, connection_end_time):
                try:
                    logger.debug(f"Creating Initiator on {ip}:{port}")
                    return await asyncio.open_connection(ip, port)
                except:
                    logger.exception(f"Failed to connect to {ip}:{port}")

            await asyncio.sleep(connection_retry)

    def start_background_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def start(self) -> asyncio.Task:
        loop = asyncio.new_event_loop()
        t = Thread(target=self.start_background_loop,
                   args=(loop,), daemon=True)
        t.start()

        event_sync = threading.Event()
        task = asyncio.run_coroutine_threadsafe(self.main(event_sync), loop)

        event_sync.wait()  # block until server is started

        return task

    def stop_all(self) -> None:
        logger.debug("Stopping All")
        self.stop_called = True
        for server, loop in self.server_map.values():
            try:
                server.close()
                future = asyncio.run_coroutine_threadsafe(
                    server.wait_closed(), loop)
                future.result()
            except:
                logger.debug("Server already closed")
        if self.engine_tasks:
            self.engine_tasks.cancel()
