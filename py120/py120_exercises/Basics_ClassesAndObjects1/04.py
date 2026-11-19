"""
Using the code from the previous exercise, add a __init__ method that prints I'm
a cat! when a new Cat object is instantiated.
"""


class Cat:
    def __init__(self):
        print(f"I'm a {self.__class__.__name__.lower()}!")


kitty = Cat()
# Expected Output: I'm a cat!
