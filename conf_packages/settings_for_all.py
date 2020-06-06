import json
import telebot
from googletrans import Translator
import time
from conf_packages.keyboard_buttons import *
import os
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
statusd = 'close'
statusw = 'close'
mode = 0
lang = 'ru'


class TokensSettings:
    def __init__(self):
        with open('config.json', 'r', encoding='utf8') as json_file:
            self.reader = json.load(json_file)

    def telegram_main_token(self):
        for token in self.reader:
            telegram_token = token['telegram_api']
            return telegram_token

    def yandex_token(self):
        for token in self.reader:
            yandex_token = token['yandex_api']
            return yandex_token

    def google_settings(self):  # This is the test format
        for settings in self.reader:
            service_urls = [settings['google_settings'][0],settings['google_settings'][1]]
            return service_urls


bot_helper = TokensSettings().telegram_main_token()
yandex_token_settings = TokensSettings().yandex_token()
google_settings = Translator(TokensSettings().google_settings())
