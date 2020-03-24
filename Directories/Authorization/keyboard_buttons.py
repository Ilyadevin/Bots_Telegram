from telebot import types


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_settings = types.KeyboardButton('Настройки')
    button_help = types.KeyboardButton('Help')
    language_english = types.KeyboardButton('en')
    language_russian = types.KeyboardButton('ru')
    language_ukrainian = types.KeyboardButton('uk')
    language_icelandic = types.KeyboardButton('is')
    language_chinese = types.KeyboardButton('zh')
    language_hindi = types.KeyboardButton('hi')
    language_arabic = types.KeyboardButton('ar')
    language_bengal = types.KeyboardButton('bn')
    language_portuguese = types.KeyboardButton('pt')
    language_indonesian = types.KeyboardButton('id')
    language_french = types.KeyboardButton('fr')
    markup.add(button_settings, button_help,
               language_english, language_russian, language_ukrainian,
               language_icelandic, language_chinese, language_hindi,
               language_arabic, language_bengal,
               language_arabic, language_bengal, language_portuguese,
               language_indonesian, language_french,
               )
    return markup
