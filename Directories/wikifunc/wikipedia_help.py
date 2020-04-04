from directories.bot_translator.settings_api import *


@bot.message_handler(content_types='text')
def getting_link(message):
    bot.send_message(message.from_user.id, f'https://en.wikipedia.org/wiki/{message.text.lower()}')
