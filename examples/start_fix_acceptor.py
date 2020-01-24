
import sys
import os
sys.path.append(os.path.join('..', '..'))
import hermes_fix as fix
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s-%(asctime)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

class FIXApp(fix.Application):
    pass

def main():
    settings = fix.SessionSettings('config.ini')
    client_app = FIXApp()
    store = fix.FileStoreFactory()
    client = fix.SocketConnection(client_app, store, settings)
    task = client.start()

    while not task.done():
        print(task.result())


if __name__ == '__main__':
    main()
