"""
Add a new setter property for name that takes either a first name or full name,
and knows how to set the first_name and last_name properties appropriately. Use
the following code to test your code:
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


bob = Person("Robert")
print(bob.name)  # Robert
print(bob.first_name)  # Robert
print(repr(bob.last_name))  # ''
bob.last_name = "Smith"
print(bob.name)  # Robert Smith

bob.name = "Prince"
print(bob.first_name)  # Prince
print(repr(bob.last_name))  # ''

bob.name = "John Adams"
print(bob.first_name)  # John
print(bob.last_name)  # Adams
