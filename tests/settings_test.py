import configparser
from conf_packages.settings_for_all import *

config = configparser.ConfigParser()
config.read('test_data.ini')
test_config = config['api_keys']['yandex']
