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

Further Exploration:
Assume you're playing a game in which cards of the same rank are unequal. In
such a game, each suit also has a ranking. Suppose that, in this game, a 4 of
Spades outranks a 4 of Hearts which outranks a 4 of Clubs which outranks a 4 of
Diamonds. A 5 of Diamonds, though, outranks a 4 of Spades since we compare ranks
first. Update the Card class so that min and max functions pick the card of the
appropriate suit if two or more cards of the same rank are present in the list.
"""


class Card:
    # Class constants
    FACE_VALUES = {
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    SUIT_VALUES = {
        "Spades": 4,
        "Hearts": 3,
        "Clubs": 2,
        "Diamonds": 1,
    }

    # Class methods, public and private
    @classmethod
    def ranking(cls, card):  # good as a kwarg in min, max, sort, reverse
        return (
            cls.FACE_VALUES.get(card.rank, card.rank),
            cls.SUIT_VALUES[card.suit],
        )

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
cards = [Card(3, "Diamonds"), Card(3, "Hearts"), Card(2, "Spades")]
print(min(cards) == Card(2, "Spades"))  # True
print(max(cards) == Card(3, "Hearts"))  # True

cards = [Card(6, "Diamonds"), Card(4, "Clubs"), Card(4, "Spades")]
print(min(cards) == Card(4, "Clubs"))  # True
print(max(cards) == Card(6, "Diamonds"))  # True

cards = [Card(4, "Spades"), Card(4, "Diamonds"), Card(10, "Diamonds")]
print(min(cards) == Card(4, "Diamonds"))  # True
print(max(cards) == Card(10, "Diamonds"))  # True

cards = [Card(7, "Diamonds"), Card("Jack", "Diamonds"), Card("Jack", "Spades")]
print(min(cards) == Card(7, "Diamonds"))  # True
print(max(cards) == Card("Jack", "Spades"))  # True

cards = [Card(8, "Diamonds"), Card(8, "Clubs"), Card(8, "Spades")]
print(min(cards) == Card(8, "Diamonds"))  # True
print(max(cards) == Card(8, "Spades"))  # True
