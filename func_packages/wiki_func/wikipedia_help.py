from conf_packages.settings_for_all import *


def getting_link(text_from_user):
    link = wikipedia.page(text_from_user.text.lower())
    return link.summary
