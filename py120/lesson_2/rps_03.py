"""
Right now, the game doesn't have very much dramatic flair. It'll be more
interesting if we were playing up to, say, 5 points. Whoever reaches 5 points
first wins. Can you build this functionality? We have a new noun -- a score. Is
that a new class, or a state of an existing class? You can explore both options
and see which one works better.

What if it was best of 5 instead of first to reach 5 wins

keep playing until 3 is in self._score

display human and computer score after each round

if human is at 2 and computer is less:
    "One more point and you win!"
if comp is at 2 and human is less:
    "One more point and the computer wins!"
if human and comp are both at 2:
    "The game is tied at 2! Next point wins!"

"""

import random


class Player:
    CHOICES = ("rock", "paper", "scissors", "q")

    def __init__(self):
        self.move = None


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt_lines = [
            "Choose a move or enter q to quit:",
            "Rock, Paper, or Scissors",
            "> ",
        ]
        prompt = "\n".join(prompt_lines)

        while True:
            choice = input(prompt).strip().lower()
            if choice in Player.CHOICES:
                break

            print(f"Sorry, {choice} is not valid")

        self.move = choice


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES[:3])


class RPSGame:
    A_BEATS_B = (
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    )

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._score = None
        self._best_of = None
        self._win_score = None
        self._match_point = None

    def _reset_score(self):
        self._score = {
            "human": 0,
            "computer": 0,
        }

    def _display_welcome_message(self):
        print(f"Welcome to Rock Paper Scissors! (Best of {self._best_of})")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors. Goodbye!")

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f"You chose: {human_move}")
        print(f"The computer chose: {computer_move}")

        if human_move == computer_move:
            print("It's a tie")
        elif (human_move, computer_move) in RPSGame.A_BEATS_B:
            print("You win this point!")
            self._score["human"] += 1
        else:
            print("Computer wins this point!")
            self._score["computer"] += 1

    def _display_score(self):
        score_lines = [
            "The score is",
            f"You: {self._score['human']}",
            f"Computer: {self._score['computer']}",
        ]
        score = "\n".join(score_lines)
        print(score)

        if self._match_point in self._score.values():
            if self._score["human"] == self._score["computer"]:
                print(
                    f"The game is tied at {self._match_point}! Next point wins!"
                )
            elif self._score["human"] == self._match_point:
                print("One more point and you win!")
            else:
                print("One more point and the computer wins!")

    def _display_overall_winner(self):
        if self._score["human"] == self._win_score:
            print(f"You win best of {self._best_of}!")
        else:
            print(f"Computer wins best of {self._best_of}!")

    def _play_again(self):
        prompt_lines = [
            f"Would you like to play best of {self._best_of} again? (y/n)",
            "> ",
        ]
        prompt = "\n".join(prompt_lines)

        while True:
            answer = input(prompt).strip().lower()
            if answer[0] in "ynq":
                return answer.startswith("y")

            print(f"{answer} is invalid")

    def _best_of_n(self):
        if (not isinstance(self._best_of, int)) or self._best_of < 3:
            self._best_of = 3
        if self._best_of % 2 == 0:
            self._best_of += 1

        self._win_score = (self._best_of + 1) // 2
        self._match_point = self._win_score - 1

    def _play_best_of(self):
        while self._win_score not in self._score.values():
            self._human.choose()
            if self._human.move == "q":
                return -1
            self._computer.choose()
            self._display_winner()
            self._display_score()

        self._display_overall_winner()

    def play(self, best_of=3):
        self._best_of = best_of
        self._best_of_n()

        self._display_welcome_message()
        self._reset_score()

        while True:
            if self._play_best_of() is not None:
                break
            if self._play_again():
                self._reset_score()
            else:
                break

        self._display_goodbye_message()


game = RPSGame()
game.play(4)
