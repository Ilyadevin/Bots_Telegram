import time

import telebot
from Directories.bot_meeting_app.settings_M import config

bot = telebot.TeleBot(config["DEFAULT"]["token"])  # Введите свой токен

mode = 0
lang = 'ru'
statusd = 'close'
statusw = 'close'
list_of_log_data = []


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! С чего начнем? /help')


@bot.message_handler(commands=['help'])
def help_user(message):
    try:
        time.sleep(2)
        bot.send_message(message.chat.id, 'Я - бот который поможет вам найти пару для приятного общения.\n'
                                          'Я использую данные из vk,\n'
                                          'Команды - "Настройки", "translate"\n')
    except Exception as error_in_command:
        print(error_in_command)


@bot.message_handler(content_types=['text'])
def setting_user(message):
    try:
        bot.send_message(message.from_user.id, 'Введите логин и пароль в формате "password login"')
        list_of_log_data.append(message.from_user.id.split(' '))
        password = list_of_log_data[0]
        login = list_of_log_data[1]
    except Exception as error_log:
        print(error_log)


bot.polling(none_stop=True)
