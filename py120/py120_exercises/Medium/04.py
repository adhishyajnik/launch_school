"""
Update the Card class so you can use it to determine the lowest ranking and
highest ranking cards in a list of Card objects.

For this exercise, numeric cards are low cards, ordered from 2 through 10. Jacks
are higher than 10s, Queens are higher than Jacks, Kings are higher than Queens,
and Aces are higher than Kings. The suit plays no part in the relative ranking
of cards.

If you have two or more cards of the same rank in your list, your min and max
methods should return one of the matching cards; it doesn't matter which one.

Besides any methods needed to determine the lowest and highest cards, create a
__str__ method that returns a string representation of the card, e.g., "Jack of
Diamonds", "4 of Clubs", etc.

---

Methods needed:
    - min (polymorphic)
        if one card underranks all others, return that card
        if there are multiple cards of the lowest rank, return any one of them
    - max (polymorphic)
        if one card outranks all others, return that card
        if there are multiple cards of the highest rank, return any one of them
    - rank
        returns the rank of the calling card
    - __str__:
        return a string concat: rank of suit
"""


class Card:
    # Class constants
    FACE_VALUES = {
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    # Class methods, public and private
    @classmethod
    def ranking(cls, card):  # good as a kwarg in min, max, sort, reverse
        return cls.FACE_VALUES.get(card.rank, card.rank)

    # Instance methods, public and private
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    # __str__ and __repr__
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({repr(self.rank)}, {repr(self.suit)})"
        )

    # Comparison dunder methods
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    # Property getters only
    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return Card.ranking(self)


# Test cases
cards = [Card(2, "Hearts"), Card(10, "Diamonds"), Card("Ace", "Clubs")]
print(min(cards) == Card(2, "Hearts"))  # True
print(max(cards) == Card("Ace", "Clubs"))  # True
print(str(min(cards)) == "2 of Hearts")  # True
print(str(max(cards)) == "Ace of Clubs")  # True

cards = [Card(5, "Hearts")]
print(min(cards) == Card(5, "Hearts"))  # True
print(max(cards) == Card(5, "Hearts"))  # True
print(str(Card(5, "Hearts")) == "5 of Hearts")  # True

cards = [Card(4, "Hearts"), Card(4, "Diamonds"), Card(10, "Clubs")]
print(min(cards).rank == 4)  # True
print(max(cards) == Card(10, "Clubs"))  # True
print(str(Card(10, "Clubs")) == "10 of Clubs")  # True

cards = [Card(7, "Diamonds"), Card("Jack", "Diamonds"), Card("Jack", "Spades")]
print(min(cards) == Card(7, "Diamonds"))  # True
print(max(cards).rank == "Jack")  # True
print(str(Card(7, "Diamonds")) == "7 of Diamonds")  # True

cards = [Card(8, "Diamonds"), Card(8, "Clubs"), Card(8, "Spades")]
print(min(cards).rank == 8)  # True
print(max(cards).rank == 8)  # True
