"""
Create a Person class with two instance variables to hold a person's first and
last names. The names should be passed to the constructor as arguments and
stored separately. The first and last names are required and must consist
entirely of alphabetic characters.

The class should also have a getter method that returns the person's name as a
full name (the first and last names are separated by spaces), with both first
and last names capitalized correctly.

The class should also have a setter method that takes the name from a
two-element tuple. These names must meet the requirements given for the
constructor.

Yes, this class is somewhat contrived.
"""


class Person:
    def __init__(self, first, last):
        self._set_name(first, last)

    @classmethod
    def _validate(cls, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.isalpha():
            raise ValueError("Name must be alphabetic.")

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"

    @name.setter
    def name(self, new_name):
        first, last = new_name
        self._set_name(first, last)

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name.title()
        self._last_name = last_name.title()


# Tests
actor = Person("Mark", "Sinclair")
print(actor.name)  # Mark Sinclair
actor.name = ("Vin", "Diesel")
print(actor.name)  # Vin Diesel
# actor.name = ("", "Diesel")
# ValueError: Name must be alphabetic.

actor.name = (5, "Diesel")
# TypeError: Name must be a string.

"""
character = Person("annIE", "HAll")
print(character.name)  # Annie Hall
character = Person("Da5id", "Meier")
# ValueError: Name must be alphabetic.
"""

"""
friend = Person("Lynn", "Blake")
print(friend.name)  # Lynn Blake
friend.name = ("Lynn", "Blake-John")
# ValueError: Name must be alphabetic.
"""
