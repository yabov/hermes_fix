import configparser
import io
from typing import Union, List
import os

configName = Union[str, dict, io.IOBase, List[str]]

class SessionSettings(configparser.ConfigParser):
    def __init__(self, config: configName) -> None:
        super().__init__()
        if isinstance(config, list) or (isinstance(config, str) and os.path.isfile(config)):
            self.read(config)
        elif isinstance(config, str):
            self.read_string(config)
        elif isinstance(config, dict):
            self.read_dict(config)
        elif isinstance(config, io.IOBase):
            self.read_file(config)
        else:
            raise TypeError(f"Config must be of type {configName}, but got type {type(config)}")

