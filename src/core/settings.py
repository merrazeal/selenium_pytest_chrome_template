import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TMP_DIR = os.path.join(BASE_DIR, "tmp")

DOWNLOADS_DIR = os.path.join(TMP_DIR, "downloads")
SCREENSHOTS_DIR = os.path.join(TMP_DIR, "screenshots")

SITE_URL = os.environ.get("SITE_URL")

TELEGRAM_CONFIG = {
    "bot_id": os.environ.get("TELEGRAM_BOT_ID"),
    "chat_id": os.environ.get("TELEGRAM_CHAT_ID"),
    "message_url": "https://api.telegram.org/bot{bot_id}/sendMessage",
    "image_url": "https://api.telegram.org/bot{bot_id}/sendPhoto",
}

TELEGRAM_NOTIFICATION = os.environ.get("TELEGRAM_NOTIFICATION") == 'True'

WEB_WAITER_DEFAULT_TIMEOUT = 5
WEB_WAITER_DOWNLOAD_TIMEOUT = 30

CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")
