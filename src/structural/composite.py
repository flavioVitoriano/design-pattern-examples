# composite example
# create a composite pipeline system

from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
from typing import List


class Component(ABC):
    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    @abstractmethod
    def execute(self):
        pass

    def is_composite(self) -> bool:
        return False


class Composite(Component):
    _childrens: List[Component]

    def __init__(self) -> None:
        self._childrens = []

    def add(self, component: Component):
        self._childrens.append(component)

    def remove(self, component: Component):
        self._childrens.remove(component)

    def execute(self):
        for child in self._childrens:
            child.execute()

    def is_composite(self) -> bool:
        return True


class Leaf(Component, metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class NormalizeStage(Leaf):
    def execute(self):
        print("Normalizing input data")


class OptmizeStage(Leaf):
    def execute(self):
        print("Optmizing the input data")


class ExecuteInputStage(Leaf):
    def execute(self):
        print("Executing with input data")


class GenerateOutputStage(Leaf):
    def execute(self):
        print("Generating output data")


if __name__ == "__main__":
    pre_pipeline = Composite()
    pre_pipeline.add(NormalizeStage())
    pre_pipeline.add(OptmizeStage())

    post_pipeline = Composite()
    post_pipeline.add(ExecuteInputStage())
    post_pipeline.add(GenerateOutputStage())

    general_pipeline = Composite()
    general_pipeline.add(pre_pipeline)
    general_pipeline.add(post_pipeline)

    # execute the pipeline
    general_pipeline.execute()
