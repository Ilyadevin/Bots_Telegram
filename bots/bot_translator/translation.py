from func_packages.translation_YA.translation import get_translate
from conf_packages.settings_for_all import *


@bot_helper.message_handler(content_types=['text'])
def settings_translate_and_result(message):
    global mode, lang
    try:
        if message.text.lower() == 'translate' or message.text.lower == '/translate':
            time.sleep(1)
            bot_helper.send_message(message.from_user.id, 'Hi there again\n'
                                                          '\n'
                                                          'Write me the word and I will translate it to you!\n'
                                                          '\n'
                                                          'I can translate the word/text or something else\n'
                                                          'On two different platforms:\n'
                                                          'Google.Translate and YandexTranslator\n'
                                                          'Translated with "Google.Translate" - \n'
                                                          'https://translate.google.com/?hl=ru,\n'
                                                          'Translated with "Яндекс.Переводчик" - \n'
                                                          'https://translate.yandex.ru,\n '
                                                          'To change the mode of translation use "settings"\n'
                                                          '\n', reply_markup=keyboard_settings())
        elif message.text.lower() == 'settings':
            time.sleep(2)
            bot_helper.send_message(message.from_user.id, 'Translation work on a few languages\n'
                                                          '\n'
                                                          'For now I use only 10 most popular languages,\n'
                                                          '\n'
                                                          '        en(English), ru(Russian), \n '
                                                          '        uk (Ukrainian), is (Icelandic), \n'
                                                          '        zh (Chinese), hi (Hindi), \n'
                                                          '        es (Spanish), ar (Arabic), \n'
                                                          '        bn (Bengali), pt (Portuguese), \n'
                                                          '        id (Indonesian), fr (French). \n'
                                                          '\n',
                                    reply_markup=keyboard()
                                    )
            bot_helper.send_message(message.from_user.id, "Choose the language.", keyboard())
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
            time.sleep(2)
            bot_helper.send_message(message.from_user.id, f'Changed to {message.text.lower()}')
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
            time.sleep(2)
            bot_helper.send_message(message.from_user.id, 'I don`t understand you,\n'
                                                          'Please, use another language\n'
                                                          '\n'
                                                          '        en(English), ru(Russian), \n '
                                                          '        uk (Ukrainian), is (Icelandic), \n'
                                                          '        zh (Chinese), hi (Hindi), \n'
                                                          '        es (Spanish), ar (Arabic), \n'
                                                          '        bn (Bengali), pt (Portuguese), \n'
                                                          '        id (Indonesian), fr (French). \n'
                                                          '\n')
        else:
            time.sleep(2)
            bot_helper.send_message(
                message.from_user.id, f'Your translation - {get_translate(message.text.lower(), lang)["text"]}\n'
                                      'Translated with "Яндекс.Переводчик" - \n'
                                      'https://translate.yandex.ru\n '
            )
            bot_helper.send_message(message.from_user.id, f'For now I use {lang}.\n'
                                                          f'If you want to change it - use settings\n')
    except Exception as error_in_text:
        bot_helper.send_message(message.from_user.id, error_in_text)
