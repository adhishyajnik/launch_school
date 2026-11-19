"""
Using the code snippet provided below, add a setter method named name. Then,
rename kitty to 'Luna' and invoke greet again.
"""


class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


kitty = Cat("Sophie")
kitty.greet()
kitty.name = "Luna"
kitty.greet()
# Expected Output:
# Hello! My name is Sophie!
# Hello! My name is Luna!
