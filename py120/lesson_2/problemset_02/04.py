"""
Using the class definition from problem 3, let's create some more people (Person
objects).

Without adding any code to the Person class, we want to compare bob and rob to
see whether they both have the same name. How can we make this comparison?
"""


class Person:
    def __init__(self, name):
        self.validate(name)
        if name == "":
            raise ValueError(
                "cannot initialize Person instance with an empty name string"
            )
        self.name = name

    @staticmethod
    def validate(string):
        if not isinstance(string, str):
            raise TypeError("cannot pass non-str type")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self.validate(first_name)
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self.validate(last_name)
        self._last_name = last_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        name_parts = name.split()
        self.first_name, self.last_name = name_parts[0], ""
        if len(name_parts) > 1:
            self.last_name = name_parts[1]
        self._name = " ".join([self.first_name, self.last_name])

    """
        def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name != other.name
    """


bob = Person("Robert Smith")
rob = Person("Robert Smith")

print(bob.name == rob.name)
