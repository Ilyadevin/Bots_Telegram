from betterconf import Config, field


class YandexApi(Config):
    yandex_api = field('trnsl.1.1.20200116T113731Z.94c83123351e649f.67da2d35fd69ce49b44b425c101fb32a83e578c5',
                         default=lambda: RuntimeError("Account's token must be defined!"))


cfg = YandexApi()