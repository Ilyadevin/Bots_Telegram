from telegram import TelegramObject


class LoginByUrl:
    def __init__(self, url, forward_text=None, bot_username=None, request_write_access=None):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access
        self.token = '837019930:AAFCyNv-WlgKQ-48dptM4rQSZ14_WxEoq5A'

        self._id_attrs = (self.url,)

    def lets_log(self):
        start_log = f'{self.url}<{self.token}/getMe'


Login = LoginByUrl('https://api.telegram.org/bot')
