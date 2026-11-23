"""
Using the code from the previous exercise, add a parameter to __init__ that
provides a name for the Cat object. Use an instance variable to print a greeting
with the provided name. (You can remove the code that displays I'm a cat!.)
"""


class Cat:
    def __init__(self, name):
        self.name = name
        print(f"Hello! My name is {self.name}!")


kitty = Cat("Sophie")
# Expected Output: Hello! My name is Sophie!
dave = Cat("Dave")
