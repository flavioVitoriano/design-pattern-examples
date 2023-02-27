# Abstract Factory example
# In this example, we will use abstract factory to determine what kind of food and wash is better for each pet in a pet store.
from abc import ABC, abstractmethod
from typing import Dict

# the abstract factory needs abstract and concrete classes for working
# in this case, we will create an abstract class Pet, and Cat and Dog as Concrete classes

# First, we need to create the Pet abstract class (or interface)
class Pet(ABC):
    # every pet speaks in different ways
    @abstractmethod
    def speak(self) -> str:
        pass


# Create the 'concrete' Pets
class Dog(Pet):
    def speak(self) -> str:
        return "auau"


class Cat(Pet):
    def speak(self) -> str:
        return "miauu"


# In the petstore, every type of animal have a different food and wash, lets create the abstract and concrete classes
# for it

# abstract Food
class Food(ABC):
    @abstractmethod
    def food_type(self) -> str:
        pass


# concrete foods

# fish ration, cat loves it
class FishRation(Food):
    def food_type(self) -> str:
        return "Wet Fish Ration"


# bone shaped ration, make your dog rise strong
class BoneShapedRation(Food):
    def food_type(self) -> str:
        return "Bone Shaped Ration"


# abstract WashType
class WashType(ABC):
    @abstractmethod
    def wash_type(self) -> str:
        pass


# concreate washtypes
class DryBath(WashType):
    def wash_type(self) -> str:
        return "Dry wash"


class CompleteBath(WashType):
    def wash_type(self) -> str:
        return "Complete wash"


# this is the abstract factory class
class AbstractPetFactory(ABC):
    @abstractmethod
    def get_pet_type(self) -> Pet:
        pass

    def get_pet_food(self) -> Food:
        pass

    def get_wash_type(self) -> WashType:
        pass


# the cat factory
class CatFactory(AbstractPetFactory):
    def get_pet_type(self) -> Pet:
        return Cat()

    def get_pet_food(self) -> Food:
        return FishRation()

    def get_wash_type(self) -> WashType:
        return DryBath()


# the dog factory
class DogFactory(AbstractPetFactory):
    def get_pet_type(self) -> Pet:
        return Dog()

    def get_pet_food(self) -> Food:
        return BoneShapedRation()

    def get_wash_type(self) -> WashType:
        return CompleteBath()


if __name__ == "__main__":
    factories: Dict[str, AbstractPetFactory] = {
        "cat": CatFactory(),
        "dog": DogFactory(),
    }

    pet_type = input("Enter your pet type [cat, dog]: ")

    try:
        factory = factories[pet_type]
        ration = factory.get_pet_food()
        pet = factory.get_pet_type()
        wash_type = factory.get_wash_type()

        print(f"Your pet says: {pet.speak()}")
        print(f"Your pet food should be: {ration.food_type()}")
        print(f"Your pet bath should be: {wash_type.wash_type()}")

    except KeyError:
        print("Invalid pet type prodived")
