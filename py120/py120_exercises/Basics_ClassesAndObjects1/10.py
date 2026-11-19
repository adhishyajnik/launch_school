"""
Create a class named Person.

When you instantiate a Person object, you should pass in one argument that
contains the person's name.

If no arguments are given, the Person object should be instantiated with a name
of "John Doe".
"""


class Person:
    def __init__(self, name="John Doe"):
        self.name = name


person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)  # John Doe
print(person2.name)  # Pepe Le Pew
