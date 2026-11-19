"""
Create a class named Cat for which calling Cat.generic_greeting prints Hello!
I'm a cat!.
"""


class Cat:
    def __init__(self):
        pass

    @classmethod
    def generic_greeting(cls):
        print(f"Hello! I'm a {cls.__name__.lower()}!")


Cat.generic_greeting()
# Hello! I'm a cat!
