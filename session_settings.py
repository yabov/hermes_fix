import configparser
from collections import OrderedDict

class SessionSettings(configparser.ConfigParser):
    def __init__ (self, file_name):
        super().__init__()
        self.read(file_name)

if __name__ == '__main__':
    settings = SessionSettings('executor.cfg')
    print (settings.sections())
    print (settings.items('SESSION1'))
    print (settings.options('SESSION2'))

    print (settings['SESSION1']['targetcompid'])