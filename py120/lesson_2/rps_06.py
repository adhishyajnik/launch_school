"""
As long as the user doesn't quit, keep track of the move history by both the
human and computer. What data structure will you reach for? Will you use a new
class, or an existing class? What will the display output look like?

history will be displayed when the user quits the program if it's not empty.

if user quits during a match rather than after the match, that match's details
should be removed from history dict and the history printed without that match
included. If dict is empty after that match is removed, don't print anything.

COL = 11

history = {
    1:  [
        ("rock", "PAPER"),
        ("SCISSORS", "paper"),
        ("rock", "rock"),
        ("PAPER", "rock"),
        "You won",
        ],
    2:  [
        ("rock", "PAPER"),
        ("SCISSORS", "paper"),
        ("rock", "rock"),
        ("paper", "SCISSORS"),
        "You lost",
        ],
}

for num in history:
    match = history[num]

    title = f"MATCH {num}: {match[-1]}"
    print(title)
    print("=" * len(title))
    print("YOU:".ljust(COL), "COMPUTER:")

    for game in match:
        print(
            game[0].ljust(COL),
            game[1]
        )

    print()


MATCH 1: You won
================
YOU:        COMPUTER:
rock        PAPER
SCISSORS    paper
rock        rock
PAPER       rock

MATCH 2: You lost
=================
YOU:        COMPUTER:
rock        PAPER
SCISSORS    paper
rock        rock
paper       SCISSORS
"""

import random


class Player:
    CHOICES = ("rock", "paper", "scissors", "lizard", "spock", "q")

    def __init__(self):
        self.move = None


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt_lines = [
            "Choose a move or enter q to quit:",
            "Rock, Paper, Scissors, Lizard, or Spock",
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
        self.move = random.choice(Player.CHOICES[:5])


class Score:
    def __init__(self):
        self.human_pts = 0
        self.computer_pts = 0
        self.match_point = None
        self.win_score = None

    def reset(self):
        self.human_pts = 0
        self.computer_pts = 0

    def add_point(self, player: Player):
        if player.__class__.__name__ == "Human":
            self.human_pts += 1
        else:
            self.computer_pts += 1

    def display(self):
        cur_score = [self.human_pts, self.computer_pts]
        if self.win_score not in cur_score:
            score_lines = [
                "The score is",
                f"You: {self.human_pts}",
                f"Computer: {self.computer_pts}",
            ]
            score = "\n".join(score_lines)
            print(score)

            if self.match_point in cur_score:
                if self.human_pts == self.computer_pts:
                    print(
                        f"The game is tied at {self.match_point}!",
                        "Next point wins!",
                    )
                elif self.human_pts == self.match_point:
                    print("One more point and you win!")
                else:
                    print("One more point and the computer wins!")


class RPSGame:
    A_BEATS_B = (
        ("rock", "scissors"),
        ("rock", "lizard"),
        ("paper", "rock"),
        ("paper", "spock"),
        ("scissors", "paper"),
        ("scissors", "lizard"),
        ("lizard", "spock"),
        ("lizard", "paper"),
        ("spock", "scissors"),
        ("spock", "rock"),
    )

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._score = Score()
        self._n_games = None

    def _display_welcome_message(self):
        print(
            "Welcome to Rock Paper Scissors Lizard Spock! (Best of",
            f"{self._n_games})",
        )

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _display_winner(self):
        human, human_move = self._human, self._human.move
        computer, computer_move = self._computer, self._computer.move

        print(f"You chose: {human_move}")
        print(f"The computer chose: {computer_move}")

        if human_move == computer_move:
            print("It's a tie")
        elif (human_move, computer_move) in RPSGame.A_BEATS_B:
            self._score.add_point(human)
            if self._score.human_pts != self._score.win_score:
                print("You win this point!")
        else:
            self._score.add_point(computer)
            if self._score.computer_pts != self._score.win_score:
                print("Computer wins this point!")

    def _display_overall_winner(self):
        if self._score.human_pts == self._score.win_score:
            print(f"You win best of {self._n_games}!")
        else:
            print(f"Computer wins best of {self._n_games}!")

    def _play_again(self):
        prompt_lines = [
            f"Would you like to play best of {self._n_games} again? (y/n)",
            "> ",
        ]
        prompt = "\n".join(prompt_lines)

        while True:
            answer = input(prompt).strip().lower()
            if answer[0] in "ynq":
                return answer.startswith("y")

            print(f"{answer} is invalid")

    def _best_of(self, n_games):
        if (not isinstance(n_games, int)) or n_games < 3:
            self._n_games = 3
        elif n_games % 2 == 0:
            self._n_games = n_games + 1
        else:
            self._n_games = n_games

        self._score.match_point = (self._n_games) // 2
        self._score.win_score = self._score.match_point + 1

    def _play_best_of(self):
        while self._score.win_score not in [
            self._score.human_pts,
            self._score.computer_pts,
        ]:
            self._human.choose()
            if self._human.move == "q":
                return "q"
            self._computer.choose()
            self._display_winner()
            self._score.display()

        self._display_overall_winner()

    def play(self, n_games=3):
        self._best_of(n_games)

        self._display_welcome_message()
        self._score.reset()

        while True:
            if self._play_best_of() == "q":
                break
            if self._play_again():
                self._score.reset()
            else:
                break

        self._display_goodbye_message()


game = RPSGame()
game.play()
