import os

import decorator

from core import settings
from adapters.notifications.telegram import TelegramNotificationSender


def telegram_notify_if_test_failed(func):
    """Web driver must be first argument."""

    def wrapper(func, *args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception:
            screenshot_path = os.path.join(
                settings.SCREENSHOTS_DIR, f"{func.__name__}.png"
            )
            args[0].save_screenshot(screenshot_path)  # web_driver
            args[0].implicitly_wait(3)
            with open(screenshot_path, "rb") as image_file:
                TelegramNotificationSender.notify(
                    recipient=settings.TELEGRAM_CONFIG["image_url"].format(
                        bot_id=settings.TELEGRAM_CONFIG["bot_id"]
                    ),
                    data={
                        "chat_id": settings.TELEGRAM_CONFIG["chat_id"],
                        "caption": f"❌ auto_test::{func.__name__} failed",
                    },
                    files={"photo": image_file},
                )
                os.remove(screenshot_path)
            raise
        return res

    return decorator.decorator(wrapper, func)
