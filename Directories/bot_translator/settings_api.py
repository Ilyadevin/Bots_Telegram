import configparser
import telebot
import time
from directories.bot_translator.keyboard_buttons import *
config = configparser.ConfigParser()
config.read('config.ini')
bot = telebot.TeleBot(config['DEFAULT']['TOKEN'])