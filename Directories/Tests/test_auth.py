import unittest
from directories.tests.settings_test import config
from directories.bot_translator.loggin_to_T import *


class TestMockBot(unittest.TestCase):
    def setUp(self):
        self.config = config['DEFAULT']['TOKEN']
        self.bot = telebot.TeleBot(self.config)

    def test_start(self):
        self.assertEqual(start_message('start'), 'Hello there! /help?')


if __name__ == '__main__':
    unittest.main()
