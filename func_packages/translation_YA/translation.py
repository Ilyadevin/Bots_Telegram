import requests
from conf_packages.settings_for_all import yandex_token_settings
token = yandex_token_settings
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def get_translate(text, lang):
    request_post = requests.post(url, data={'key': token, 'text': text, 'lang': lang})
    response_data = request_post.json()
    return response_data
