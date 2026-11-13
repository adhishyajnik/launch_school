"""
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class.
The class should have at least one instance variable that gets initialized by
the initializer.

What class you create doesn't matter, provided it satisfies the above
requirements.
"""


class Person:
    def __init__(self, name):
        self.name = name
        type_name = self.__class__.__name__
        print(f"I am {name}, a {type_name}.")


class Primitive:
    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f"This is a {name}, a {type_name.lower()}.")


class Cube(Primitive):
    def roll(self):
        print(f"The {self.name} rolled onto a different face.")


class Sphere(Primitive):
    def roll(self):
        print(f"It's hard to tell how much the {self.name} rolled.")


class Cylinder(Primitive):
    def knock(self):
        print(f"The {self.name} was knocked over and is rollable")


mike = Person("Mike")
anna = Person("Anna")

dice = Cube("D6")
ball = Sphere("dodgeball")
dowel = Cylinder("toilet paper tube")

dice.roll()
ball.roll()
dowel.knock()
