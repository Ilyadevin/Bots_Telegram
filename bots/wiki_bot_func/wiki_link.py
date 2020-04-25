from func_packages.wiki_func.wikipedia_help import *


@bot_helper.message_handler(content_types=['text'])
def link_to_user(message):
    try:
        time.sleep(2)
        bot_helper.send_message(message.from_user.id, f'Searching Wikipedia for {getting_link(message)}')
    except wikipedia.exceptions.DisambiguationError as error_in_link:
        time.sleep(1)
        bot_helper.send_message(message.from_user.id, f'There is an unexpected error:\n'
                                                      f'{error_in_link}')
        bot_helper.send_message(message.from_user, 'DisambiguationError: The page name is ambiguous')
