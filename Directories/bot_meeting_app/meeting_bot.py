import telebot
from directories.bot_translator.keyboard_buttons import keyboard_settings_meeting
from directories.bot_meeting_app.settings_M import config
import time
bot = telebot.TeleBot(config["DEFAULT"]["token"])  # Введите свой токен

mode = 0
statusd = 'close'
statusw = 'close'
list_of_log_data = []


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! С чего начнем?',
                     reply_markup=keyboard_settings_meeting()
                     )


