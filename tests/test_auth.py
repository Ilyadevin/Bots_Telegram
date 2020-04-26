import unittest
from tests.settings_test import test_config_helper_bot
from bots.telegram_main_file import *


class TestMockBot(unittest.TestCase):
    def setUp(self):
        self.config = test_config_helper_bot
        self.bot = telebot.TeleBot(self.config)

    def tearDownClass(self):
        try:
            os.remove(self.config)
        except OSError as oserror:
            print(oserror)

    def test_start(self):
        self.assertEqual(start_message('start'), 'Hello there! /help?')


if __name__ == '__main__':
    unittest.main()
