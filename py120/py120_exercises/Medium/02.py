"""
Create an object-oriented number guessing class for numbers in the range 1 to
100, with a limit of 7 guesses per game. The game should play as follows.

Note that a game object should start a new game with a new number to guess with
each call to play.
"""

import random


class GuessingGame:
    GUESSES = 7
    RANGE_MIN = 1
    RANGE_MAX = 100
    REMAIN = "You have {0} {1} remaining."  # 0: int, 1: "guess" or "guesses"
    PROMPT = f"Enter a number between {RANGE_MIN} and {RANGE_MAX}: "
    INVALID = f"Invalid guess. {PROMPT}"
    TOO_HI = "Your guess is too high.\n"
    TOO_LO = "Your guess is too low.\n"
    MATCH = "That's the number!\n"
    WIN = "You won!\n"
    LOSE = "You have no more guesses. You lost!\n"

    def __init__(self):
        self._number = None
        self._rem_guesses = 0

    @classmethod
    def _is_valid(cls, guess):
        return (guess.strip().isdigit()) and (
            cls.RANGE_MIN <= int(guess) <= cls.RANGE_MAX
        )

    @staticmethod
    def _pluralize(number):
        return "guess" if number == 1 else "guesses"

    def _reset(self):
        random.seed()
        self._number = random.randint(self.RANGE_MIN, self.RANGE_MAX)
        self._rem_guesses = self.GUESSES

    def _make_guess(self):
        guess = input(self.PROMPT)
        while not self._is_valid(guess):
            guess = input(self.INVALID)
        self._rem_guesses -= 1
        return int(guess)

    def _check_guess(self, guess):
        if guess < self._number:
            return self.TOO_LO
        elif guess > self._number:
            return self.TOO_HI
        else:
            return self.MATCH

    def _print_remaining(self, remaining):
        print(self.REMAIN.format(remaining, self._pluralize(remaining)))

    def _game_play(self):
        while self._rem_guesses:
            self._print_remaining(self._rem_guesses)
            guess_result = self._check_guess(self._make_guess())
            print(guess_result)
            if guess_result == self.MATCH:
                return self.WIN
        return self.LOSE

    def play(self):
        self._reset()
        game_result = self._game_play()
        print(game_result)


game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!
