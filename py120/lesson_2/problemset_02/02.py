"""
Modify the class definition from above to facilitate the following methods. Note
that there is no name= setter method now.
"""


class Person:
    def __init__(self, name):
        self.validate(name)
        if name == "":
            raise ValueError(
                "cannot initialize Person instance with an empty name string"
            )
        name_parts = name.strip().split()
        self.first_name, self.last_name = name_parts[0], ""
        if len(name_parts) > 1:
            self.last_name = name_parts[1]

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
        return f"{self.first_name} {self.last_name}".strip()


bob = Person("Robert")
print(bob.name)  # Robert
print(bob.first_name)  # Robert
print(repr(bob.last_name))  # ''
bob.last_name = "Smith"
print(bob.name)  # Robert Smith
