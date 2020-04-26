import unittest
from func_packages.translation_YA.translation import get_translate
from mock import patch
from tests.settings_test import test_config_yandex


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.configuration_token = test_config_yandex
        self.example_translation = {'text': 'Привет', 'lang': 'ru-en'}
        self.example_wrong_text = {'text': "апыаппрварпсгеси щшгпр"}

    def test_200(self):
        result = get_translate(self.example_translation['text'],
                               self.example_translation['lang'])
        self.assertEqual(result['code'], 200)

    def test_translation(self):
        result_translate = get_translate(self.example_translation['text'],
                                         self.example_translation['lang'])
        self.assertTrue(result_translate['text'], 'Hi')

    def test_block_api(self):
        with patch(self.configuration_token) as _:
            result = get_translate(self.example_translation['text'],
                                   self.example_translation['lang'])['code']
            self.assertTrue(result, 402)

    def test_wrong_api(self):
        with patch(self.configuration_token.join('1234567')) as _:
            result = get_translate(self.example_translation['text'],
                                   self.example_translation['lang'])['code']
            self.assertTrue(result, 401)

    def test_wrong_text(self):
        result = get_translate(self.example_wrong_text['text'],
                               self.example_translation['lang'])
        self.assertTrue(result['code'], 422)
