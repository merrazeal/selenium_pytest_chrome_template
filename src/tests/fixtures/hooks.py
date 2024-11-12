import logging

from adapters.notifications.telegram import TelegramNotificationSender
from core import settings


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == 0:
        logging.info("all tests passed")
        TelegramNotificationSender.notify(
            recipient=settings.TELEGRAM_CONFIG["message_url"].format(
                bot_id=settings.TELEGRAM_CONFIG["bot_id"]
            ),
            data={
                "chat_id": settings.TELEGRAM_CONFIG["chat_id"],
                "text": "✅ auto_test::all tests passed",
            },
        )
