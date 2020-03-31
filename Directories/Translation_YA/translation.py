import requests
from directories.translation_YA.settings_YA import config

token = 'trnsl.1.1.20200328T163033Z.f4042c658559a62e.49edfe4bc90d1db9282e7abe9359ceff6a1b15e8'
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def get_translate(text, lang):
    TEXT = text
    LANG = lang
    request_post = requests.post(url, data={'key': token, 'text': TEXT, 'lang': LANG})
    response_data = request_post.json()

    return response_data
