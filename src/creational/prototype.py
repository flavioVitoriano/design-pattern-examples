# Prototype Example
from __future__ import annotations
from abc import ABC
from typing import Tuple


class Actor(ABC):
    attack_points: int
    hp: int
    # tuple containing x,y position
    position: Tuple(int, int)

    def __init__(self, hp: int, attack_points: int, position: Tuple(int, int)) -> None:
        self.attack_points = attack_points
        self.hp = hp
        self.position = position

    @classmethod
    def from_actor(cls, actor: Actor) -> Actor:
        return Actor(
            hp=actor.hp,
            attack_points=actor.attack_points,
            position=actor.position,
        )

    # in this example, we will use the previous classmethod for doing the clone, but, in python, you could use the 'deepcopy'
    # function from the 'copy' library instead.
    def clone(self) -> Actor:
        # if using the deepcopy
        # return deepcopy(self)
        return self.from_actor(self)


class Goblin(Actor):
    def __init__(self, position: Tuple(int, int)) -> None:
        super().__init__(20, 6, position)


class Caracter(Actor):
    name: str

    def __init__(
        self, hp: int, attack_points: int, position: Tuple(int, int), name: str
    ) -> None:
        super().__init__(hp, attack_points, position)
        self.name = name

    @classmethod
    def from_actor(cls, actor: Caracter) -> Caracter:
        return Caracter(
            hp=actor.hp,
            attack_points=actor.attack_points,
            position=actor.position,
            name=actor.name,
        )

    def clone(self) -> Caracter:
        return super().clone()


if __name__ == "__main__":
    protagonist = Caracter(100, 10, (1, 1), name="Flavin")
    # create another caracter using clone
    paladin = protagonist.clone()
    paladin.name = "Cecil the Paladin"

    # a horde of enemies
    enemy_1 = Goblin(position=(2, 2))
    enemy_2 = enemy_1.clone()
    enemy_3 = enemy_1.clone()

    # tests if all refers to the same object
    assert enemy_1 is not enemy_2
    assert enemy_2 is not enemy_3
    assert enemy_3 is not enemy_1

    assert protagonist is not paladin

    assert protagonist.name != paladin.name

    print("all working properly!")
