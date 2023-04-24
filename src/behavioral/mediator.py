from __future__ import annotations
from typing import Dict


class BaseComponent:
    mediator: BaseMediator

    def execute(self):
        raise NotImplementedError("This is a abstract class")

    def __str__(self):
        return self.__class__.__name__


class BaseMediator:
    def notify(self, sender: BaseComponent, event: str):
        raise NotImplementedError("This is a abstract class")


class CloseButton(BaseComponent):
    def execute(self):
        self.mediator.notify(self, "on_close")


class SendButton(BaseComponent):
    def execute(self):
        self.mediator.notify(self, "on_send")


class UploadWindowDialog(BaseMediator):
    def __init__(self, close_button: BaseComponent, send_button: BaseComponent) -> None:
        self._close_button = close_button
        self._send_button = send_button
        self._close_button.mediator = self
        self._send_button.mediator = self

    def on_close(self):
        print("Closing window...")

    def on_send(self):
        print("Uploading files...")

    def notify(self, sender: BaseComponent, event: str):
        callbacks: Dict[str, function] = {
            "on_close": self.on_close,
            "on_send": self.on_send,
        }

        print(f"Event received: '{sender}' - '{event}'")

        if event in callbacks.keys():
            callbacks[event]()


if __name__ == "__main__":
    close_button = CloseButton()
    send_button = SendButton()

    dialog = UploadWindowDialog(close_button, send_button)

    close_button.execute()
    send_button.execute()
