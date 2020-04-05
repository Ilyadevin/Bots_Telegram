from bots.bot_translator.translation import *
from func_packages.wiki_func.wikipedia_help import *


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        time.sleep(1)
        bot.send_message(message.chat.id, 'Hello there! /help?',
                         reply_markup=keyboard_settings()
                         )
    except Exception as error_in_command:
        bot.send_message(message.chat.id, error_in_command)


@bot.message_handler(commands=['help'])
def help_user(message):
    try:
        time.sleep(1)
        bot.send_message(message.chat.id, 'I can help you with some tasks.\n'
                                          'Now I can translate texts into the language you need.\n'
                                          'Not everything in the world ;)\n'
                                          'Commands - "Settings" , "translate"\n'
                                          "WARNING - I'm using Russian Language as main\n",
                         reply_markup=keyboard_settings()
                         )
        settings_translate_and_result()
    except Exception as error_in_command:
        bot.send_message(message.chat.id, error_in_command)


@bot.message_handler(commands=['wiki'])
def wiki_check(message):
    try:
        time.sleep(1)
        bot.send_message(message.chat.id, 'Here some func of wiki request\n'
                                          'You give me the word and give you a link\n')
        getting_link()
    except Exception as error:
        bot.send_message(message.chat.id, error)


@bot.message_handler(commands=['info'])
def info(message):
    bot.message_handler(message.chat.id,
                        "Hello, I'm the one who made this bot.\n"
                        "For now it`s giving you the translation of the words you need.\n"
                        "Later I will add new functions.\n"
                        "If you have some advices let me know on:\n"
                        "https://t.me/erlihigh\n"
                        "https://github.com/Ilyadevin\n"
                        "Good Luck!", reply_markup=keyboard_settings()
                        )
