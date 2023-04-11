# strategy pattern example

from typing import Any


# we define a base interface for strategies
class BaseMessagingStrategy:
    def export(self, data: Any):
        raise NotImplementedError("Abstract class")


# the concrete strategies
class SocketMessagingStrategy(BaseMessagingStrategy):
    def export(self, data: Any):
        """messaging logic with socket"""
        print("sending data with socket strategy")


class IRCMessagingStrategy(BaseMessagingStrategy):
    def export(self, data: Any):
        """messaging logic with IRC"""
        print("sending data with IRC strategy")

class AMQPMessagingStrategy(BaseMessagingStrategy):
    def export(self, data: Any):
        """messaging logic with AMQP"""
        print("sending data with AMQP strategy")   

# using the strategy, we can separate the messaging logic from the application class
# and there is no need to modify the Application class when a new messaging logic is implemented
class Application:
    messaging_strategy: BaseMessagingStrategy

    def __init__(self, message_strategy: BaseMessagingStrategy) -> None:
        self.messaging_strategy = message_strategy