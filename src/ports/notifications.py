from abc import ABC, abstractmethod


class BaseNotificationSender(ABC):
    @classmethod
    @abstractmethod
    def notify(self, recipient, data, **kwargs): ...
