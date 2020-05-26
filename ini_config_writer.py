import configparser
import tempfile

class IniConfigWriter:
    ''' INI Config Writer '''

    json_config = {}

    def __init__(self, json_config):
        self.json_config = json_config

    def get_temporary_ini_file(self):
        with tempfile.NamedTemporaryFile(suffix='.ini') as temp_file_path:
            return temp_file_path.name

    def create_config(self):
        config = configparser.ConfigParser()
        config['default'] = { 
            'Profile' : self.json_config['basic_profile_settings']['profile'],
            'MarketWatch' : self.json_config['basic_profile_settings']['market_watch'],
            'Server' : self.json_config['basic_profile_settings']['server'],
            'EnableDDE' : self.json_config['basic_profile_settings']['enable_ddf'],
            'EnableNews' : self.json_config['basic_profile_settings']['enable_news'],
            'ExpertsEnable' : self.json_config['expert_settings']['experts_enable'],
            'ExpertsDllImport' : self.json_config['expert_settings']['experts_dll_import'],
            'ExpertsExpImport' : self.json_config['expert_settings']['experts_exp_import'],
            'ExpertsTrades' : self.json_config['expert_settings']['experts_trades'],
            'TestExpert' : self.json_config['strategy_tester_settings']['test_expert'],
            'TestSymbol' : self.json_config['strategy_tester_settings']['test_symbol'],
            'TestPeriod' : self.json_config['strategy_tester_settings']['test_period'],
            'TestModel' : self.json_config['strategy_tester_settings']['test_model'],
            'TestSpread' : self.json_config['strategy_tester_settings']['test_spread'],
            'TestOptimization' : self.json_config['strategy_tester_settings']['test_optimization'],
            'TestDateEnable' : self.json_config['strategy_tester_settings']['test_data_enable'],
            'TestFromDate' : self.json_config['strategy_tester_settings']['test_date_range_from'],
            'TestToDate' : self.json_config['strategy_tester_settings']['test_date_range_to'],
            'TestReport' : self.json_config['strategy_tester_settings']['test_report'],
            'TestReplaceReport' : self.json_config['strategy_tester_settings']['test_replace_report'],
            'TestShutdownTerminal' : self.json_config['strategy_tester_settings']['test_shutdown_terminal'],
             }

        login = self.json_config['basic_profile_settings']['login']
        if login:
            config['default']['login'] = login

        password = self.json_config['basic_profile_settings']['password']
        if password:
            config['default']['password'] = password

        auto_configuration = self.json_config['basic_profile_settings']['auto_configuration']
        if auto_configuration:
            config['default']['AutoConfiguration'] = auto_configuration

        data_server = self.json_config['basic_profile_settings']['data_server']
        if data_server:
            config['default']['DataServer'] = data_server

        test_expert_parameters = self.json_config['strategy_tester_settings']['test_expert_parameters']
        if test_expert_parameters:
            config['default']['TestExpertParameters'] = test_expert_parameters

        ini_file_path = self.get_temporary_ini_file()

        with open(ini_file_path, 'w') as configfile:
            config.write(configfile)

        # Removing the 'default' section from the output INI file as there is no way to have INI file without section using configparser
        with open(ini_file_path, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(ini_file_path, 'w') as fout:
            fout.writelines(data[1:])

        return ini_file_path
