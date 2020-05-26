import json
import os.path
from os import path
import sys

class ConfigFileParser:
    ''' Config File Parser '''

    config_file_path = ""

    def __init__(self, config_file_path):
        if not path.exists(config_file_path):
            raise Exception(f'Config file "{config_file_path}" does not exist')

        self.config_file_path = config_file_path

    def load_config(self):
        print(f'Loading config file "{self.config_file_path}" ...')
        
        with open(self.config_file_path) as f:
            return json.load(f)
