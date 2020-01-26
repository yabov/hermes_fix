import configparser

class SessionSettings(configparser.ConfigParser):
    def __init__ (self, file_name : str) -> None:
        super().__init__()
        self.read(file_name)
