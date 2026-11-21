"""
In the previous two exercises, you developed a Card class and a Deck class. You
are now going to use those classes to create and evaluate poker hands. Create a
class, PokerHand, that takes 5 cards from a Deck of Cards and evaluates those
cards as a poker hand.

You should build your class using the following code skeleton.

The exact cards and the type of hand for the first test will vary with each run,
so don't expect the same output we show for the first 6 lines.

Some variants of Poker allow both Ace-high (A, K, Q, J, 10) and Ace-low (A, 2,
3, 4, 5) straights. For simplicity, your code only needs to recognize Ace-high
straights.
♣♥♦♠

.-----. .-----. .-----. .-----. .-----.
|2    | |2    | |2    | |2    | |2    |
|  ♣  | |  ♣  | |  ♣  | |  ♣  | |  ♣  |
|    2| |    2| |    2| |    2| |    2|
'-----' '-----' '-----' '-----' '-----'
"""

# Include Card and Deck classes from the last two exercises.
from random import shuffle


class Deck:
    RANKS = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self):
        self._reset()

    def _reset(self):
        self._deck = [
            Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS
        ]
        shuffle(self._deck)

    def draw(self):
        if not self._deck:
            self._reset()
        return self._deck.pop()


class Card:
    # Class constants
    FACE_VALUES = {
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    SUIT_SYMBOLS = {
        "Spades": "♠",
        "Hearts": "♥",
        "Clubs": "♣",
        "Diamonds": "♦",
    }

    # Class methods, public and private
    @classmethod
    def ranking(cls, card):  # good as a kwarg in min, max, sort, reverse
        if not isinstance(card, Card):
            return NotImplemented
        return cls.FACE_VALUES.get(card.rank, card.rank)

    @classmethod
    def symbol(cls, card):
        if not isinstance(card, Card):
            return NotImplemented
        return cls.SUIT_SYMBOLS.get(card.suit, card.suit[0])

    # Dunder instance methods
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({repr(self.rank)}, {repr(self.suit)})"
        )

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return (self.value, self.suit) == (other.value, other.suit)

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    # rank, suit, and value getters
    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return Card.ranking(self)

    @property
    def glyph(self):
        return Card.symbol(self)


class PokerHand:
    def __init__(self, deck: Deck):
        self._hand = sorted([deck.draw() for _ in range(5)])
        self._ranks = [card.rank for card in self._hand]
        self._values = [card.value for card in self._hand]
        self._unq_suits = set(card.suit for card in self._hand)
        self._unq_ranks = set(self._ranks)

    def print(self):
        for card in self._hand:
            print(card)

    def show_cards(self):
        line1_base = ".-----."
        line2_base = "|{0}   |"
        line3_base = "|  {0}  |"
        line4_base = "|   {0}|"
        line5_base = "'-----'"

        line1 = " ".join([line1_base] * len(self._hand)).center(79)
        line5 = " ".join([line5_base] * len(self._hand)).center(79)

        line2_strings, line4_strings = [], []
        for card in self._hand:
            rank_str = str(card.rank)
            if rank_str == "10":
                line2_strings.append(line2_base.format(rank_str))
                line4_strings.append(line4_base.format(rank_str))
            else:
                line2_strings.append(line2_base.format(rank_str[0].ljust(2)))
                line4_strings.append(line4_base.format(rank_str[0].rjust(2)))
        line2 = " ".join(line2_strings).center(79)
        line4 = " ".join(line4_strings).center(79)

        line3 = " ".join(
            [line3_base.format(card.glyph) for card in self._hand]
        ).center(79)

        print("\n".join(["", line1, line2, line3, line4, line5, ""]))

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _is_straight(self):
        # 5-rank sequence of more than one suit
        min_value = min(self._values)
        return set(self._values) == set(range(min_value, min_value + 5))

    def _is_flush(self):
        # all cards of the same suit
        return len(self._unq_suits) == 1

    def _is_straight_flush(self):
        # any 5 rank sequence of the same suit except A K Q J 10
        return self._is_straight() and self._is_flush()

    def _is_royal_flush(self):
        # A K Q J 10 of same suit
        return self._is_straight_flush() and "Ace" in self._ranks

    def _is_n_of_a_kind(self, n: int, numeric=False):
        # n cards of the same rank
        counts = [self._ranks.count(rank) for rank in self._unq_ranks]
        if numeric:
            return counts.count(n)
        return n in counts

    def _is_four_of_a_kind(self):
        # 4 cards of the same rank
        return self._is_n_of_a_kind(4)

    def _is_three_of_a_kind(self):
        # 3 cards of the same rank
        return self._is_n_of_a_kind(3)

    def _is_pair(self):
        # 1 pair of the same rank
        return self._is_n_of_a_kind(2, True) == 1

    def _is_full_house(self):
        # 3 cards of one rank, 2 cards of another
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_two_pair(self):
        # 2 pairs of 2 different ranks
        return self._is_n_of_a_kind(2, True) == 2


# Test cases
hand = PokerHand(Deck())
hand.print()
hand.show_cards()
print(hand.evaluate())
print()


# Adding TestDeck class for testing purposes
class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards


# All of these tests should return True
hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")


"""
EXPECTED OUTPUT:
5 of Clubs
7 of Diamonds
Ace of Hearts
7 of Clubs
5 of Spades
Two pair

True
True
True
True
True
True
True
True
True
True
True
True
True
"""
