import configparser
config = configparser.ConfigParser()
config.read('test_data.ini')
config_yandex=config['DEFAULT']['TOKEN']