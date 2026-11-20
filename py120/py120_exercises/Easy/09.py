"""
Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently
some of our users are nobility, and the regular way of walking simply isn't good
enough. Nobility struts.

We need a new class Noble that shows the title and name when walk is called. We
also require access to name and title; they are needed for other purposes that
we aren't showing here.
"""


class WalkMixin:
    def walk(self):
        return f"{self} {self._gait()} forward"


class Person(WalkMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name

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


class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def _gait(self):
        return "saunters"


class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def _gait(self):
        return "runs"


byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)  # "Byron"
print(byron.title)  # "Lord"
