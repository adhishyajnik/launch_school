"""
Create a class named Cat that tracks the number of times a new Cat object is
instantiated. The total number of Cat instances should be printed when total is
invoked.
"""


class Cat:
    num_cats = 0

    def __init__(self):
        self.__class__.num_cats += 1

    @classmethod
    def total(cls):
        return Cat.num_cats


print(Cat.total())  # 0

kitty1 = Cat()
print(Cat.total())  # 1

kitty2 = Cat()
print(Cat.total())  # 2

print(Cat())  # <__main__.Cat object at 0x104ed7290>
print(Cat.total())  # 3
