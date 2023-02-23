# Builder example
# In this code, i will try to create a user builder. this builder will help building User objects.
# We also are creating nested builders, like AddressBuilder and PhoneBuilder
# Note: in this case, we are putting business logic into builders methods (The input validation). Actually exists better ways to do this.
# But lets keep this way in this case, for the sake of simplicity.
from __future__ import annotations
from datetime import date
from typing import List, Optional, Tuple


# The user can have many addresses
class Address:
    street: str
    number: int

    def __init__(self, street: str, number: int) -> None:
        self.street = street
        self.number = number


# The user class
class User:
    first_name: str
    last_name: str
    birthdate: date
    addresses: List[Address]
    phones: List[str]

    def __init__(self) -> None:
        self.addresses = []
        self.phones = []

    @staticmethod
    def builder() -> UserBuilder:
        return UserBuilder()


# let create the builders
class PhoneBuilder:
    phones: List[str]

    def __init__(self, phones: List[str] = None) -> None:
        if not phones:
            phones = []
        self.phones = phones

    def add(self, phone: str) -> PhoneBuilder:
        if not phone.isnumeric():
            raise ValueError(
                f"The phone {phone} contain invalid caracters. Make sure they have only numbers"
            )

        self.phones.append(phone)
        return self

    def build(self) -> List[str]:
        return self.phones


class AddressBuilder:
    # we will use tuple for easily verify if a address is already submited
    addresses: List[Tuple(str, int)]

    def __init__(self, addresses: List[Address] = None) -> None:
        if not addresses:
            self.addresses = []

        # convert address format to tuple
        self.addresses = [(addr.street, addr.number) for addr in addresses]

    def add(self, street: str, number: int) -> AddressBuilder:
        new_address_raw = (street, number)

        if new_address_raw in self.addresses:
            raise ValueError(
                f"The address {street}, {number} is already registered for this user"
            )

        self.addresses.append(new_address_raw)
        return self

    def build(self) -> List[Address]:
        # in the build, we can return a list of Address Objects
        addresses = [Address(addr[0], addr[1]) for addr in self.addresses]

        return addresses


class UserBuilder:
    phones: PhoneBuilder
    addresses: AddressBuilder

    def __init__(self, user: Optional[User] = None) -> None:
        if user is not None:
            self.user = user
        self.user = User()
        self.phones = PhoneBuilder(self.user.phones)
        self.addresses = AddressBuilder(self.user.addresses)

    def first_name(self, value: str) -> UserBuilder:
        self.user.first_name = value
        return self

    def last_name(self, value: str) -> UserBuilder:
        self.user.last_name = value
        return self

    def birthdate(self, birthdate: date) -> UserBuilder:
        if birthdate > date.today():
            raise ValueError("Invalid birthdate date")
        self.user.birthdate = date
        return self

    def build(self) -> User:
        self.user.phones = self.phones.build()
        self.user.addresses = self.addresses.build()

        return self.user


if __name__ == "__main__":
    builder = User.builder()

    # basic information
    (builder.first_name("Saruman").last_name("The white").birthdate(date.today()))

    # phones
    (builder.phones.add("55555555").add("66666666").add("77777777"))

    # validation error - invalid characters at number
    try:
        builder.phones.add("85-555555")
    except ValueError as e:
        print(e)

    # addresses
    (
        builder.addresses.add("nowhere", 123)
        .add("vaga lumes", 456)
        .add("rua das flores", 567)
    )

    # validation error - address already registered
    try:
        builder.addresses.add("vaga lumes", 456)
    except ValueError as e:
        print(e)

    # with the builder, whe can get the complete user object
    user = builder.build()

    print(f"Full name: {user.first_name} {user.last_name}")
    print(f"Phones: {user.phones}")
    print(f"Main address: {user.addresses[0].street} {user.addresses[0].number}")
