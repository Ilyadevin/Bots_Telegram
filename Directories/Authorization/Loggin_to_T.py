import telebot
from Directories.Authorization.keyboard_buttons import keyboard as keyboard_btn
from Directories.Translation_YA.translation import *

bot = telebot.TeleBot('837019930:AAFCyNv-WlgKQ-48dptM4rQSZ14_WxEoq5A')  # Введите свой токен
mode = 0
lang = 'ru'
statusd = 'close'
statusw = 'close'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! С чего начнем? /help')


@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.chat.id, 'Я - бот который поможет вам облегчить жизнь в контексте некоторых задач.\n'
                                      'Сейчас я умею переводить тексты на нужный вам язык.\n'
                                      'Но пока что, к сожалению не все на свете ;)\n'
                                      'Команды - "Настройки", "translate"\n')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global mode, lang
    if message.text.lower() == 'translate' or message.text.lower == '/translate':
        bot.send_message(message.from_user.id, 'Привет ещё раз ;)\n'
                                               'Я бот - который переводит слова и тексты,\n'
                                               'напиши мне что ты хочешь перевести и я сделаю это!\n'
                                               'Переведено сервисом "Яндекс.Переводчик" - https://translate.yandex.ru\n'
                                               'Чтобы настроить перевод, используйте, пожалуйста - настройки\n')
    elif message.text.lower() == 'настройки':
        bot.send_message(message.from_user.id, 'Перевод работает на нескольких языках,\n'
                                               'на данный момент поддерживаются 10 самых популярных языков мира,\n'
                                               'выберите на какой перевеодить.\n'
                                               'Доступные на данный момент:\n'
                                               '        en(Английский), ru(Русский),\n'
                                               '        uk(Украинский), is(Исландский),\n'
                                               '        zh(Китайский), hi(Хинди),\n'
                                               '        es(Испанский), ar(Арабский),\n'
                                               '        bn(Бенгальский), pt(Португальский),\n'
                                               '        id(Индонезийский), fr(Французский).\n'
                         )
        bot.send_message(message.from_user.id, "Выберите нужный язык.", keyboard_btn())
        mode = 1
    elif mode == 1 and message.text.lower() == 'en' \
            or mode == 1 and message.text.lower() == 'hi' \
            or mode == 1 and message.text.lower() == 'es' \
            or mode == 1 and message.text.lower() == 'ar' \
            or mode == 1 and message.text.lower() == 'bn' \
            or mode == 1 and message.text.lower() == 'pt' \
            or mode == 1 and message.text.lower() == 'id' \
            or mode == 1 and message.text.lower() == 'fr' \
            or mode == 1 and message.text.lower() == 'is' \
            or mode == 1 and message.text.lower() == 'ru' \
            or mode == 1 and message.text.lower() == 'zh' \
            or mode == 1 and message.text.lower() == 'uk':
        bot.send_message(message.from_user.id, f'Переключаю на {message.text.lower()}')
        lang = message.text.lower()
        mode = 0
    elif mode == 1 and message.text.lower() != 'en' \
            or mode == 1 and message.text.lower() != 'ru' \
            or mode == 1 and message.text.lower() != 'uk' \
            or mode == 1 and message.text.lower() != 'hi' \
            or mode == 1 and message.text.lower() != 'es' \
            or mode == 1 and message.text.lower() != 'ar' \
            or mode == 1 and message.text.lower() != 'bn' \
            or mode == 1 and message.text.lower() != 'pt' \
            or mode == 1 and message.text.lower() != 'id' \
            or mode == 1 and message.text.lower() != 'fr' \
            or mode == 1 and message.text.lower() != 'is' \
            or mode == 1 and message.text.lower() != 'zh':
        bot.send_message(message.from_user.id, 'Я не понял твой язык, введите другой.\n'
                                               'ПОДДЕРЖИВАЕМЫЕ язык: \n'
                                               'en(Английский), ru(Русский), uk(Украинский),\n'
                                               'is(Исландский), zh(Китайский), hi(Хинди),\n'
                                               'es(Испанский), ar(Арабский),bn(Бенгальский),\n'
                                               'pt(Португальский), id(Индонезийский), fr(Французский).\n')
    else:
        bot.send_message(
            message.from_user.id, f'Ваш перевод - {get_translate(message.text.lower(), lang)["text"]}\n'
                                  f'Переведено сервисом "Яндекс.Переводчик" - https://translate.yandex.ru'
        )
        bot.send_message(message.from_user.id, f'Сейчас я использую {lang}.\n'
                                               f'Если вы хотите изменить язык используйте - настройки.\n')


bot.polling(none_stop=True)
