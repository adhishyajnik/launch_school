"""
Update this code so you see the following output when you run the code:

My cat Cocoa is 3 years old and has black fur.
My cat Cheddar is 4 years old and has yellow and white fur.
"""


class Pet:
    def __init__(self, name, age, colors):
        self._name = name
        self._age = age
        self._colors = colors.lower()

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def colors(self):
        return self._colors

    @property
    def info(self):
        type_name = self.__class__.__name__.lower()
        name, age, colors = self.name, self.age, self.colors
        return (
            f"My {type_name} {name} is {age} years old and has {colors} fur."
        )


class Cat(Pet):
    pass


cocoa = Cat("Cocoa", 3, "black")
cheddar = Cat("Cheddar", 4, "yellow and white")

print(cocoa.info)
print(cheddar.info)
