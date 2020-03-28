from __future__ import absolute_import

import unittest

import telegram
from telegram import ChatAction
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import InlineQueryResult
from telegram import TelegramError
from telegram import User, Message, Chat, Update
from telegram.ext import Updater, CommandHandler

from ptbtest import Mockbot


class TestMockBot(unittest.TestCase):
    def setUp(self):
        self.mock_bot = Mockbot()

    def test_updater_works_with_mock_bot(self):
        # handler method
        def start(bot, update):
            message = bot.sendMessage(update.message.chat_id, "this works")
            self.assertIsInstance(message, Message)

            updater = Updater(workers=2, bot=self.mockbot)
            dp = updater.dispatcher
            dp.add_handler(CommandHandler("start", start))
            updater.start_polling()
            user = User(id=1, first_name="test")
            chat = Chat(45, "group")
            message = Message(
                404, user, None, chat, text="/start", bot=self.mockbot)
            message2 = Message(
                404, user, None, chat, text="start", bot=self.mockbot)
            message3 = Message(
                404, user, None, chat, text="/start@MockBot", bot=self.mockbot)
            message4 = Message(
                404, user, None, chat, text="/start@OtherBot", bot=self.mockbot)
            self.mockbot.insertUpdate(Update(0, message=message))
            self.mockbot.insertUpdate(Update(1, message=message2))
            self.mockbot.insertUpdate(Update(1, message=message3))
            self.mockbot.insertUpdate(Update(1, message=message4))
            data = self.mockbot.sent_messages
            self.assertEqual(len(data), 2)
            data = data[0]
            self.assertEqual(data['method'], 'sendMessage')
            self.assertEqual(data['chat_id'], chat.id)
            updater.stop()


if __name__ == '__main__':
    unittest.main()
