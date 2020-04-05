from conf_packages.settings_for_all import *
import wikipedia


@bot.message_handler(content_types='text')
def getting_link(message):
    bot.send_message(message.from_user.id, f'Searching Wikipedia for {message.text}')
    try:
        time.sleep(2)
        bot.send_message(message.from_user.id, wikipedia.page(f'https://en.wikipedia.org/wiki/{message.text.lower()}'))
    except wikipedia.exceptions.DisambiguationError as error_in_link:
        bot.send_message(message.from_user.id, error_in_link)
        bot.send_message(message.from_user, 'DisambiguationError: The page name is ambiguous')
