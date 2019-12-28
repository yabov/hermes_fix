import asyncio
import logging
import fix_message_library
import threading
from threading import Thread
from fix_engine import FIXEngineInitiator, FIXEngineAcceptor


logger = logging.getLogger(__name__)

class SocketConnection:
    def __init__(self, application, storeFactory, settings):
        self.settings = settings
        self.application = application
        self.storeFactory = storeFactory
        self.server_map = {}
        self.client_map = {}
        self.settings_map = {}
        self.session_settings = settings
        self.lock = None
        self.engine_tasks = None

    async def on_connected_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        sockname = writer.get_extra_info('sockname')
        logger.info(f'Accepted New Connection on [{sockname}]<-->[{addr}]')
        engine = FIXEngineAcceptor(self.application, self.storeFactory, self.session_settings, reader, writer)
        try:
            await engine.serve_client()
        except Exception as e:
            logger.exception(e)
        writer.close()
        logger.info(f"Ending Connection on [{sockname}]<-->[{addr}]")
        await writer.wait_closed()

    async def main(self, event_sync):

        engines = []
        self.lock = asyncio.Lock()
        for section in self.settings.sections():
            if self.settings[section]['ConnectionType'] == 'acceptor':
                engines.append(self.start_acceptor(section))
            elif self.settings[section]['ConnectionType'] == 'initiator':
                engines.append(self.start_initiator(section))

        self.engine_tasks = asyncio.gather(*engines)
        event_sync.set()
        try:
            await self.engine_tasks
        except:
            pass


    async def start_acceptor(self, section):
        logger.debug(f"Starting Acceptor Session [{section}]...")
        ip = self.settings[section].get('SocketAcceptHost', 'localhost')
        port = self.settings[section]['SocketAcceptPort']
        server = None
        async with self.lock:
            if (ip, port) in self.server_map:
                logger.debug(f"Server already created on {ip}:{port}")
                server = self.server_map[(ip, port)]
                self.settings_map[(self.settings[section]['SenderCompID'], self.settings[section]['TargetCompID'])] = self.settings[section]
                return
            else:
                logger.debug(f"Creating Acceptor on {ip}:{port}")
                server = await asyncio.start_server(self.on_connected_client, ip, port)
                self.server_map[(ip,port)] = server

        addr = server.sockets[0].getsockname()
        logger.debug(f"Connection Created, serving on {addr}")

        async with server:
            try:
                await server.serve_forever()
                #await asyncio.gather(server.serve_forever())
            except asyncio.CancelledError:
                pass
        logger.debug("Ending Server")


    async def start_initiator(self, section):
        logger.debug(f"Starting Initiator Session [{section}]...")
        ip = self.settings[section]['SocketConnectHost']
        port = self.settings[section]['SocketConnectPort']
        reader = None
        writer = None
        if (ip, port) in self.client_map:
            logger.debug(f"Client already created on {ip}:{port}")
            reader, writer = self.client_map[(ip, port)]
        else:
            logger.debug(f"Creating Initiator on {ip}:{port}")
            try:
                reader, writer = await asyncio.open_connection(ip, port)
            except:
                logger.exception(f"Failed to connect to {ip}:{port}")
            self.client_map[(ip,port)] = (reader, writer)

        self.settings_map[(self.settings[section]['SenderCompID'], self.settings[section]['TargetCompID'])] = self.settings[section]
        addr = writer.get_extra_info('peername')
        sockname = writer.get_extra_info('sockname')
        engine = FIXEngineInitiator(self.application, self.storeFactory, self.session_settings, reader, writer, self.settings[section])
        try:
            await engine.send_logon()
            await engine.serve_client()
        except asyncio.streams.ConnectionResetError:
            logger.error("Server Closed Connection")
        except:
            logger.exception("Error in client")
        writer.close()
        logger.info(f"Ending Connection on [{sockname}]<-->[{addr}]")
        await writer.wait_closed()

    def start_background_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()


    def start(self):
        loop = asyncio.new_event_loop()
        t = Thread(target=self.start_background_loop, args=(loop,), daemon=True)
        t.start()

        event_sync = threading.Event()
        task = asyncio.run_coroutine_threadsafe(self.main(event_sync), loop)
        
        event_sync.wait() #block until server is started

        return task
        

    def stop_all(self):
        logger.debug("Stopping All")
        for server in self.server_map.values():
            try:
                server.close() 
            except:
                logger.debug("Server already closed")
        self.engine_tasks.cancel()

        


