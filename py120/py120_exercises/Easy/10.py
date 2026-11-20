"""
Modify the House class so the program works as shown in the expected results.
"""


class House:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __eq__(self, other):
        if isinstance(other, House):
            return self.price == other.price
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.price != other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.price < other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.price > other.price
        return NotImplemented


home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")

"""
EXPECTED OUTPUT:
Home 1 is cheaper
Home 2 is more expensive
"""
