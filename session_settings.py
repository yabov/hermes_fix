import configparser

class SessionSettings(configparser.ConfigParser):
    def __init__ (self, file_name):
        super().__init__()
        self.read(file_name)
