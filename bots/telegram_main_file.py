from bots.bot_translator.translation import *
from bots.wiki_bot_func.wiki_link import *


@bot_helper.message_handler(commands=['start'])
def start_message(message):
    try:
        time.sleep(1)
        bot_helper.send_message(message.chat.id, 'Hello there! /help?',
                                reply_markup=keyboard_settings()
                                )
    except Exception as error_in_command:
        bot_helper.send_message(message.chat.id, error_in_command)


@bot_helper.message_handler(commands=['help'])
def help_user(message):
    try:
        time.sleep(1)
        bot_helper.send_message(message.chat.id, 'I can help you with some tasks.\n'
                                                 '\n'
                                                 'Now I can translate texts into the language you need.\n'
                                                 'Not everything in the world ;)\n'
                                                 '\n'
                                                 'Commands - "Settings" , "translate", "wiki"\n'
                                                 "WARNING - I'm using Russian Language as main\n"
                                                 '\n'
                                                 "As for Wiki-functions - you can write something\n"
                                                 "So I`ll give you a link to article about it\n",
                                reply_markup=keyboard_settings()
                                )
        settings_translate_and_result()
    except Exception as error_in_command:
        bot_helper.send_message(message.chat.id, error_in_command)


@bot_helper.message_handler(commands=['wiki'])
def wiki_check(message):
    try:
        time.sleep(1)
        bot_helper.send_message(message.chat.id, 'Here some func of wiki request\n'
                                                 'You give me the word and give you a link\n')
        link_to_user()
    except Exception as error:
        bot_helper.send_message(message.chat.id, error)


@bot_helper.message_handler(commands=['info'])
def info(message):
    bot_helper.message_handler(message.chat.id,
                               "Hello, I'm the one who made this bot.\n"
                               "For now it`s giving you the translation of the words you need.\n"
                               "Later I will add new functions.\n"
                               "If you have some advices let me know on:\n"
                               "\n"
                               "https://t.me/erlihigh\n"
                               "https://github.com/Ilyadevin\n"
                               "Good Luck!", reply_markup=keyboard_settings()
                               )
    bot_helper.send_message(message.chat.id, 'Also you can help me with development\n'
                                             'Just contact me with those methods above\n'
                                             'Thanks for using my bot :)')
