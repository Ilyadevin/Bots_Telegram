from betterconf import Config, field


class TelegramKey(Config):
    telegram_api = field('837019930:AAFCyNv-WlgKQ-48dptM4rQSZ14_WxEoq5A',
                         default=lambda: RuntimeError("Account's token must be defined!"))


cfg = TelegramKey()
