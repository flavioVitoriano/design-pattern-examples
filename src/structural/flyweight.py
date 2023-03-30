from typing import Dict


class CarFlyweight:
    def __init__(self, state: list) -> None:
        self._state = state


class CarFactory:
    _cars: Dict[str, CarFlyweight] = {}

    def __init__(self, initial_state: list) -> None:
        for state in initial_state:
            self._cars[self._get_hash(state)] = CarFlyweight(state)

    def _get_hash(self, state: list) -> str:
        return ".".join(sorted(state))

    def __getitem__(self, state: list) -> CarFlyweight:
        car_hash = self._get_hash(state)

        if not self._cars.get(car_hash, None):
            print("Creating new flyweight")
            self._cars[car_hash] = CarFlyweight(state)
            return self._cars[car_hash]

        print("Return existing flyweight")
        return self._cars[car_hash]

    def __str__(self) -> str:
        print("Cars: " + ", ".join(self._cars.keys))


if __name__ == "__main__":
    factory = CarFactory([
        ["BMW", "Blue"],
        ["Focus", "Yellow"],
        ["Kwid", "Silver"]
    ])

    existing_flyweight = factory[["BMW", "Blue"]]
    new_flyweight = factory[["Focus", "Blue"]]
