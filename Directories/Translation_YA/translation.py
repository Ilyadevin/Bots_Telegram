import requests
from directories.translation_YA.settings_YA import config

token = config["DEFAULT"]["token"]
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def get_translate(text, lang):
    TEXT = text
    LANG = lang
    request_post = requests.post(url, data={'key': token, 'text': TEXT, 'lang': LANG})
    response_data = request_post.json()

    return response_data
