import configparser
import telebot
from googletrans import Translator
import time
import wikipedia
from conf_packages.keyboard_buttons import *
import os
statusd = 'close'
statusw = 'close'
mode = 0
list_of_log_data = []


def yandex_c():
    config_ya = configparser.ConfigParser()
    config_ya.read('config_YA.ini')
    config_yandex = config_ya['api_keys']['yandex']
    return config_yandex


def meeting_c():
    config_m = configparser.ConfigParser()
    config_m.read('config_M.ini')
    config_meeting = config_m['api_keys']['TOKEN']
    return config_meeting


bot_meeting = telebot.TeleBot(meeting_c())


def helper_c():
    config_t = configparser.ConfigParser()
    config_t.read('config.ini')
    config_telegram = config_t['api_keys']['helper_bot']
    return config_telegram


bot_helper = telebot.TeleBot(helper_c())


def google_settings():
    google_translation = Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.kr',
    ])
    return google_translation
