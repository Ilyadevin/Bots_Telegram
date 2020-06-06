import requests
from conf_packages.settings_for_all import yandex_token_settings
token = yandex_token_settings
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def get_translate(text, lang):
    TEXT = text
    LANG = lang
    request_post = requests.post(url, data={'key': token, 'text': TEXT, 'lang': LANG})
    response_data = request_post.json()

    return response_data
