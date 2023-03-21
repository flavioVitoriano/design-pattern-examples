# decorator example
# based on the example provided by refactoring guru
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class ConsoleNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"Console: {message}")


class NotifierDecorator(Notifier, metaclass=ABCMeta):
    _notifier: Notifier

    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class SMSNotifierDecorator(NotifierDecorator):
    def notify(self, message: str) -> None:
        print(f"SMS: {message}")
        self._notifier.notify(message)


class SlackNotifierDecorator(NotifierDecorator):
    def notify(self, message: str) -> None:
        print(f"Slack: {message}")
        self._notifier.notify(message)


class WhatsappNotifierDecorator(NotifierDecorator):
    def notify(self, message: str) -> None:
        print(f"Whatsapp: {message}")
        self._notifier.notify(message)


if __name__ == "__main__":
    # lets suppose we need to send a message using all notifiers
    console = ConsoleNotifier()
    sms_decorator = SMSNotifierDecorator(console)
    slack_decorator = SlackNotifierDecorator(sms_decorator)
    whatsapp_decorator = WhatsappNotifierDecorator(slack_decorator)

    whatsapp_decorator.notify("Notifying all ways possible!")
