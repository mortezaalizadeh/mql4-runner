#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Morteza Alizadeh"
__version__ = "0.1.0"
__license__ = "GPL 3.0"

import argparse
import os
from config_file import ConfigFileParser
from ini_config_writer import IniConfigWriter

def main(args):
    """ Main entry point of the app """

    try:
        config  = ConfigFileParser(args.config_file_path).load_config()

        for test_symbol in config['strategy_tester_settings']['test_symbols']:
            for date_range in config['strategy_tester_settings']['test_date_ranges']:
                config['strategy_tester_settings']['test_symbol'] = test_symbol
                config['strategy_tester_settings']['test_date_range_from'] = date_range['from']
                config['strategy_tester_settings']['test_date_range_to'] = date_range['to']

                ini_config_file_parser = IniConfigWriter(config).create_config()
                os.system(f'"{args.terminal_file_path}" {ini_config_file_parser}')
    
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("terminal_file_path", help="Terminal file path")
    parser.add_argument("config_file_path", help="Config file path")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
