from conf_packages.settings_for_all import *

bot = telebot.TeleBot(meeting_c())  # Введите свой токен

mode = 0
statusd = 'close'
statusw = 'close'
list_of_log_data = []


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there! Lets start?',
                     reply_markup=keyboard_settings_meeting()
                     )
