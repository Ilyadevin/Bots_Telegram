import time

import telebot
from directories.bot_translator.settings_api import config
from directories.bot_translator.keyboard_buttons import keyboard_settings
from directories.translation_YA.translation import get_translate

bot = telebot.TeleBot(config['DEFAULT']['TOKEN'])  # Введите свой токен


statusd = 'close'
statusw = 'close'


@bot.message_handler(commands=['start'])
def start_message(message):
    time.sleep(1)
    bot.send_message(message.chat.id, 'Привет! С чего начнем?',
                     reply_markup=keyboard_settings()
                     )


@bot.message_handler(commands=['help'])
def help_user(message):
    try:
        time.sleep(1)
        bot.send_message(message.chat.id, 'Я - бот который поможет вам облегчить жизнь в контексте некоторых задач.\n'
                                          'Сейчас я умею переводить тексты на нужный вам язык.\n'
                                          'Но пока что, к сожалению не все на свете ;)\n'
                                          'Команды - "Настройки", "translate"\n',
                         reply_markup=keyboard_settings()
                         )
    except Exception as error_in_command:
        print(error_in_command)
