"""
Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently
some of our users are nobility, and the regular way of walking simply isn't good
enough. Nobility struts.

We need a new class Noble that shows the title and name when walk is called. We
also require access to name and title; they are needed for other purposes that
we aren't showing here.

Further Exploration
This exercise can be solved in a similar manner by using inheritance; a Noble is
a Person, and a Cheetah is a Cat, and both Persons and Cats are Animals. What
changes would you need to make to this program to establish these relationships
and eliminate the two duplicated __str__ methods?

Is __str__ the best way to provide the name and title functionality we needed
for this exercise? Might it be better to create either a different name method
(or say a new full_name method) that automatically accesses title and name
attributes? There are tradeoffs with each choice -- they are worth considering.
"""


class WalkMixin:
    def walk(self):
        return f"{self} {self._gait()} forward"


class Animal(WalkMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name


class Person(Animal):
    def __init__(self, name):
        super().__init__(name)

    def _gait(self):
        return "strolls"


class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self._title = title

    @property
    def title(self):
        return self._title

    def __str__(self):
        return f"{self.title} {self.name}"

    def _gait(self):
        return "struts"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def _gait(self):
        return "saunters"


class Cheetah(Cat):
    def __init__(self, name):
        super().__init__(name)

    def _gait(self):
        return "runs"


byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)  # "Byron"
print(byron.title)  # "Lord"
