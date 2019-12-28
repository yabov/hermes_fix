import sys
import fix
import logging

class Application(fix.Application):
    pass



logging.basicConfig(level=logging.DEBUG)


file = sys.argv[1]
settings = fix.SessionSettings( file )
application = Application()
storeFactory = fix.FileStoreFactory()
acceptor = fix.SocketAcceptor( application, storeFactory, settings )
acceptor.start()