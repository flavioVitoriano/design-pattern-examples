from __future__ import annotations
from typing import Any, List


class Memento:
    """The Memento class will store the internal state of Originator objects"""

    _state: Any

    def __init__(self, state: Any) -> None:
        self._state = state

    @property
    def state(self) -> Any:
        return self._state


class Originator:
    """The Originator objects represent the instances we want to keep the state"""

    _state: Any

    def __init__(self, state: Any) -> None:
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.state


class CareTaker:
    """The CareTaker object will  manage the snapshots (mementos) and will be responsible to handle the state of originator"""

    _originator: Originator
    _history: List[Memento]

    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._history = []

    def add_snapshot(self) -> Memento:
        memento = self._originator.save()
        self._history.append(memento)
        return memento

    def undo_snapshot(self) -> Memento:
        memento = self._history.pop()
        return memento
