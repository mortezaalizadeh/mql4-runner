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
        ini_file_path = self.get_temporary_ini_file()

        with open(ini_file_path, 'w') as configfile:
            configfile.write(';--------- BASIC PROFILE SETTINGS\n')
            configfile.write(f'Profile={self.json_config["basic_profile_settings"]["profile"]}\n')
            configfile.write(f'MarketWatch={self.json_config["basic_profile_settings"]["market_watch"]}\n')

            login = self.json_config['basic_profile_settings']['login']
            if login:
                configfile.write(f'Login={login}\n')
            else:
                configfile.write(';Login=\n')

            password = self.json_config['basic_profile_settings']['password']
            if password:
                configfile.write(f'Password={password}\n')
            else:
                configfile.write(';Password=\n')

            configfile.write(f'Server={self.json_config["basic_profile_settings"]["server"]}\n')

            auto_configuration = self.json_config['basic_profile_settings']['auto_configuration']
            if auto_configuration:
                configfile.write(f'AutoConfiguration={auto_configuration}\n')
            else:
                configfile.write(';AutoConfiguration=\n')

            data_server = self.json_config['basic_profile_settings']['data_server']
            if data_server:
                configfile.write(f'DataServer={data_server}\n')
            else:
                configfile.write(';DataServer=\n')

            if self.json_config['basic_profile_settings']['enable_ddf']:
                configfile.write('EnableDDE=true\n')
            else:
                configfile.write('EnableDDE=false\n')

            if self.json_config['basic_profile_settings']['enable_news']:
                configfile.write('EnableNews=true\n')
            else:
                configfile.write('EnableNews=false\n')

            configfile.write('\n')
            configfile.write(';--------- EXPERT SETTINGS\n')

            if self.json_config['expert_settings']['experts_enable']:
                configfile.write('ExpertsEnable=true\n')
            else:
                configfile.write('ExpertsEnable=false\n')

            if self.json_config['expert_settings']['experts_dll_import']:
                configfile.write('ExpertsDllImport=true\n')
            else:
                configfile.write('ExpertsDllImport=false\n')

            if self.json_config['expert_settings']['experts_exp_import']:
                configfile.write('ExpertsExpImport=true\n')
            else:
                configfile.write('ExpertsExpImport=false\n')

            if self.json_config['expert_settings']['experts_trades']:
                configfile.write('ExpertsTrades=true\n')
            else:
                configfile.write('ExpertsTrades=false\n')

            configfile.write('\n')
            configfile.write('\n')
            configfile.write(';--------- STRATEGY TESTER SETTINGS\n')
            configfile.write(f'TestExpert={self.json_config["strategy_tester_settings"]["test_expert"]}\n')

            test_expert_parameters = self.json_config['strategy_tester_settings']['test_expert_parameters']
            if test_expert_parameters:
                configfile.write(f'TestExpertParameters={test_expert_parameters}\n')
            else:
                configfile.write(';TestExpertParameters=\n')

            configfile.write(f'TestSymbol={self.json_config["strategy_tester_settings"]["test_symbol"]}\n')
            configfile.write(f'TestPeriod={self.json_config["strategy_tester_settings"]["test_period"]}\n')
            configfile.write(f'TestModel={self.json_config["strategy_tester_settings"]["test_model"]}\n')
            configfile.write(f'TestSpread={self.json_config["strategy_tester_settings"]["test_spread"]}\n')

            if self.json_config['strategy_tester_settings']['test_optimization']:
                configfile.write('TestOptimization=true\n')
            else:
                configfile.write('TestOptimization=false\n')

            if self.json_config['strategy_tester_settings']['test_data_enable']:
                configfile.write('TestDateEnable=true\n')
            else:
                configfile.write('TestDateEnable=false\n')

            configfile.write(f'TestFromDate={self.json_config["strategy_tester_settings"]["test_date_range_from"]}\n')
            configfile.write(f'TestToDate={self.json_config["strategy_tester_settings"]["test_date_range_to"]}\n')
            configfile.write(f'TestReport={self.json_config["strategy_tester_settings"]["test_report"]}\n')

            if self.json_config['strategy_tester_settings']['test_replace_report']:
                configfile.write('TestReplaceReport=true\n')
            else:
                configfile.write('TestReplaceReport=false\n')

            if self.json_config['strategy_tester_settings']['test_shutdown_terminal']:
                configfile.write('TestShutdownTerminal=true\n')
            else:
                configfile.write('TestShutdownTerminal=false\n')

        return ini_file_path
