from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Subscriber
class BaseObserver(ABC):
    @abstractmethod
    def update(self, state: dict):
        pass


# Publisher
class BaseSubject(ABC):
    listeners: List[BaseObserver]
    state: dict

    def __init__(self, initial_state: dict = None) -> None:
        self.listeners = []
        self.state = initial_state

        if not initial_state:
            self.state = {}

    def subscribe(self, observer: BaseObserver):
        self.listeners.append(observer)

    def unsubscribe(self, observer: BaseObserver):
        self.listeners.remove(observer)

    def notify_all(self):
        for observer in self.listeners:
            print(f"{observer.__class__.__name__} notified!")
            observer.update(self.state)


# notify all listeners if a game is on sale
class GameOnSalePublisher(BaseSubject):
    def set_game_on_sale(self, game: str, value: float):
        self.state[game] = value
        self.notify_all()


class SendEmailObserver(BaseObserver):
    def update(self, state: dict):
        print("Sending email for interested customers")


class UpdateShopWithPricesObserver(BaseObserver):
    def update(self, state: dict):
        print("Updating store with the new values")


# example
if __name__ == "__main__":
    publisher = GameOnSalePublisher({})
    publisher.subscribe(SendEmailObserver())
    publisher.subscribe(UpdateShopWithPricesObserver())

    publisher.set_game_on_sale("fallout new vegas", 9.99)
