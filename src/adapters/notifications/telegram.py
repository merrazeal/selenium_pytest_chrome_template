import logging

import requests

from core import settings
from ports.notifications import BaseNotificationSender


class TelegramNotificationSender(BaseNotificationSender):

    @classmethod
    def notify(self, recipient, data, *args, **kwargs):
        if settings.TELEGRAM_NOTIFICATION:
            try:
                with requests.post(recipient, data=data, *args, **kwargs) as response:
                    response.raise_for_status()
            except Exception as e:
                logging.error(f"error sending request to telegram: {e}")
            else:
                logging.info(f"telegram request sent successfully")
