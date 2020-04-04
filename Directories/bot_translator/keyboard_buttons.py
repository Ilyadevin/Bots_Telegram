from telebot import types


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
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
    markup.add(
        language_english, language_russian, language_ukrainian,
        language_icelandic, language_chinese, language_hindi,
        language_arabic, language_bengal,
        language_arabic, language_portuguese,
        language_indonesian, language_french,
    )
    return markup


def keyboard_settings():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_settings = types.KeyboardButton('settings')
    button_help = types.KeyboardButton('/help')
    markup.add(button_help, button_settings)
    return markup


def keyboard_settings_meeting():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_settings = types.KeyboardButton('settings')
    button_help = types.KeyboardButton('/help')
    button_meeting = types.KeyboardButton('Meet')
    button_info = types.ReplyKeyboardMarkup('info')
    markup.add(button_help,
               button_settings,
               button_meeting,
               button_info)
    return markup


def wiki_settings():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_wiki_settings = types.KeyboardButton('wiki func')
    return markup.add(button_wiki_settings)
