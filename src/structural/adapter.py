# Adapter pattern example
# This example is a system that can predict intents based on the client phrases
import abc
from typing import List
from random import Random


# In this example, we can have many prediction services, and they share a common interface.

# The interface
class SystemPredictService(abc.ABC):
    @abc.abstractmethod
    def predict_phrases(self, phrases: List[str]) -> List[str]:
        pass


# But, the actual predicition service we have is already done, and it not follow the previous interface.
# Let's imagine that is not possible or viable do modifications in the actual prediction service.

# The actual predicition service
class ExternalPredictionService:
    _possible_intents: List[str] = [
        "greeting",
        "offense",
        "repair",
        "restart",
        "shutdown",
        "add_feature",
    ]
    # Note: this method only allow one phrase per call
    def predict(self, phrase: str):
        # In this case, lets return a random intent for each phrase, just for the example
        random = Random(len(phrase))
        return random.choice(self._possible_intents)


# To resolve this, we can create an adapter class, this one will adapt the current prediction service with the expected
# from the interface.
class ExternalPredictionServiceAdapter(SystemPredictService):
    def __init__(self, adaptee: ExternalPredictionService) -> None:
        self._adaptee = adaptee

    # Now we can use the same business logic of 'ExternalPredictionService', but using the same interface expected from the system
    # and with no modification on it!
    def predict_phrases(self, phrases: List[str]) -> List[str]:
        intents = [self._adaptee.predict(phrase=phrase) for phrase in phrases]
        return intents


if __name__ == "__main__":
    external_prediction_service = ExternalPredictionService()
    prediction_adapter = ExternalPredictionServiceAdapter(external_prediction_service)

    intents = prediction_adapter.predict_phrases(
        ["hello from above", "is this the real life?", "or it is just fantasy?"]
    )

    assert len(intents) == 3
    print(intents)
