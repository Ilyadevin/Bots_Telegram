from conf_packages.settings_for_all import *


@bot_meeting.message_handler(commands=['start'])
def start_message(message):
    bot_meeting.send_message(message.chat.id, 'Hello there! Lets start?',
                             reply_markup=keyboard_settings_meeting()
                             )
