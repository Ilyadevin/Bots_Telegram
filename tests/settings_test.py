import configparser
from conf_packages.settings_for_all import *

config = configparser.ConfigParser()
config.read('test_data.ini')
test_config_yandex = config['api_keys']['yandex']
test_config_helper_bot = config['api_keys']['helper_bot']
test_config_meeting_bot = config['api_keys']['meeting_bot']
