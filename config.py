import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6783270820:AAFlvrEd3ErcZE7A348fqZW2ZA9iqGV2hho")

    APP_ID = int(os.environ.get("APP_ID", 16314924))

    API_HASH = os.environ.get("API_HASH", "f4940cd3b12d4433abf0da0518970472")
