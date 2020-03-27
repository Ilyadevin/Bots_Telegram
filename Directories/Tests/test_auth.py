from __future__ import absolute_import

import unittest
from Directories.Authorization.Loggin_to_T import *

import unittest

from ptbtest import (BadBotException, BadCallbackQueryException,
                     BadUserException, BadMessageException)
from ptbtest import (CallbackQueryGenerator, MessageGenerator, Mockbot,
                     UserGenerator)
from telegram import (CallbackQuery, Message, Update, User)


class Test_case(unittest.TestCase):
    def setUp(self) -> None:
        self.example_callback=CallbackQueryGenerator()
        self.example_set = {'first_message': 'start'}

    # test for answer
    def test_answer(self):
        with self.assertRaisesRegexp(BadCallbackQueryException, 'message and inline_message_id'):
            self.example_callback.get_callback_query()
        with self.assertRaisesRegexp(BadCallbackQueryException,
                                     "message and inline_message_id"):
            self.example_callback.get_callback_query(message=True, inline_message_id=True)
