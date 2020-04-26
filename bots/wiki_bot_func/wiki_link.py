from func_packages.wiki_func.wikipedia_help import *


@bot_helper.message_handler(content_types=['text'])
def link_to_user(message):
    try:
        time.sleep(1)
        bot_helper.send_message(message.from_user.id, f'Searching Wikipedia for {message}')
        time.sleep(0.5)
        bot_helper.send_message(message.from_user.id, f'Small information about your request\n'
                                                      f'{getting_link(message).summary[0:70]}\n'
                                                      f'Link for more - {getting_link(message).fullurl}')
    except Exception as error_in_link:
        time.sleep(1)
        bot_helper.send_message(message.from_user.id, f'There is an unexpected error:\n'
                                                      f'{error_in_link}')
        bot_helper.send_message(message.from_user, 'DisambiguationError: The page name is ambiguous')
