"""
Create an object-oriented number guessing class for numbers in the range 1 to
100, with a limit of 7 guesses per game. The game should play as follows.

Note that a game object should start a new game with a new number to guess with
each call to play.
"""

import random
import math


class GuessingGame:
    REMAIN = "You have {0} {1} remaining."  # int, "guess" or "guesses"
    PROMPT = "Enter a number between {0} and {1}: "  # self._low, self._high
    INVALID = "Invalid guess."
    ABOVE = "Your guess is too high.\n"
    BELOW = "Your guess is too low.\n"
    MATCH = "That's the number!\n"
    W = "You won!\n"
    L = "You have no more guesses. You lost!\n"

    def __init__(self, low, high):
        self._low = low
        self._high = high
        self._prompt = self.PROMPT.format(low, high)
        self._number = None
        self._max_guesses = int(math.log2(high - low + 1)) + 1
        self._rem_guesses = 0

    @staticmethod
    def _pluralize(number):
        return "guess" if number == 1 else "guesses"

    def _print_remaining(self, remaining):
        print(self.REMAIN.format(remaining, self._pluralize(remaining)))

    def _reset(self):
        random.seed()
        self._number = random.randint(self._low, self._high)
        self._rem_guesses = self._max_guesses

    def _is_valid(self, guess):
        return (guess.strip().isdigit()) and (
            self._low <= int(guess) <= self._high
        )

    def _make_guess(self):
        guess = input(self._prompt)
        while not self._is_valid(guess):
            guess = input(f"{self.INVALID} {self._prompt}")
        return int(guess)

    def _check_guess(self, guess):
        if guess < self._number:
            return self.BELOW
        elif guess > self._number:
            return self.ABOVE
        else:
            return self.MATCH

    def _game_play(self):
        while self._rem_guesses:
            self._print_remaining(self._rem_guesses)
            guess_result = self._check_guess(self._make_guess())
            print(guess_result)
            self._rem_guesses -= 1

            if guess_result == self.MATCH:
                return self.W

        return self.L

    def play(self):
        self._reset()
        game_result = self._game_play()
        print(game_result)


game = GuessingGame(501, 1500)
game.play()

"""
You have 10 guesses remaining.
Enter a number between 501 and 1500: 104
Invalid guess. Enter a number between 501 and 1500: 1000
Your guess is too low.

You have 9 guesses remaining.
Enter a number between 501 and 1500: 1250
Your guess is too low.

You have 8 guesses remaining.
Enter a number between 501 and 1500: 1375
Your guess is too high.

You have 7 guesses remaining.
Enter a number between 501 and 1500: 80
Invalid guess. Enter a number between 501 and 1500: 1312
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 501 and 1500: 1343
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 501 and 1500: 1359
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 501 and 1500: 1351
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 501 and 1500: 1355
That's the number!

You won!
"""

game.play()

"""
You have 10 guesses remaining.
Enter a number between 501 and 1500: 1000
Your guess is too high.

You have 9 guesses remaining.
Enter a number between 501 and 1500: 750
Your guess is too low.

You have 8 guesses remaining.
Enter a number between 501 and 1500: 875
Your guess is too high.

You have 7 guesses remaining.
Enter a number between 501 and 1500: 812
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 501 and 1500: 843
Your guess is too high.

You have 5 guesses remaining.
Enter a number between 501 and 1500: 820
Your guess is too low.

You have 4 guesses remaining.
Enter a number between 501 and 1500: 830
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 501 and 1500: 835
Your guess is too low.

You have 2 guesses remaining.
Enter a number between 501 and 1500: 836
Your guess is too low.

You have 1 guess remaining.
Enter a number between 501 and 1500: 837
Your guess is too low.

You have no more guesses. You lost!
"""
