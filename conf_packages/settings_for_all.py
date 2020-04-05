import configparser
import telebot
import time
from conf_packages.keyboard_buttons import *
statusd = 'close'
statusw = 'close'


def yandex_c():
    config_ya = configparser.ConfigParser()
    config_ya.read('config_YA.ini')
    config_yandex = config_ya['DEFAULT']['TOKEN']
    return config_yandex


def meeting_c():
    config_m = configparser.ConfigParser()
    config_m.read('config_M.ini')
    config_meeting = config_m['DEFAULT']['TOKEN']
    return config_meeting


config_t = configparser.ConfigParser()
config_t.read('config.ini')
config_telegram = config_t['DEFAULT']['TOKEN']
bot = telebot.TeleBot(config_telegram)