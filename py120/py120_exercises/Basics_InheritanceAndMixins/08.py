"""
Using the code below, determine the method resolution order (MRO) will use to
access the cat1.get_color method. Note that there is no get_color property
anywhere in the listed classes. Do not use the mro method nor the __mro__
attribute.

- Cat class
- Animal class
- object class
- raise AttributeError
"""


class Animal:
    def __init__(self, color):
        self._color = color


class Cat(Animal):
    pass


class Bird(Animal):
    pass


cat1 = Cat("Black")
print(cat1.get_color())
