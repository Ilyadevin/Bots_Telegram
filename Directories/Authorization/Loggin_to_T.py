import telebot
from directories.translation_YA.translation import get_translate

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! С чего начнем? /help')


@bot.message_handler(commands=['help'])
def help_desk(message):
    bot.send_message(message.chat.id, 'Вот функции с которыми я могу тебе помочь: /translate - перевод текста')


@bot.message_handler(commands=['translate'])
def translation_helper(message):
    bot.send_message(message.chat.id, 'Что ты хочешь перевести? ')

    @bot.message_handler(content_types=['text'])
    def translation(message_to_translate):
        bot.send_message(message.chat.id, f"Твой перевод - {get_translate(message_to_translate.text, 'en-ru')['text']}")


bot.polling()
