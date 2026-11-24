import random


class ConsoleMixin:
    @property
    def width(self):
        return 55


class Rules:
    RULES = [
        "RULES:",
        "Rock beats Scissors",
        "Scissors beats Paper",
        "Paper beats Rock",
    ]


class Player(ConsoleMixin):
    PROMPT = [
        "",
        "Choose a number from 1 to 3 or q to quit",
        "",
        "1. Rock   2. Paper   3. Scissors",
    ]
    INVALID = ["", "Invalid choice."]

    def __init__(self, player_type):
        self.player_type = player_type

    def choose(self):
        if self.player_type == "human":
            choice = self._move()
            if choice == "q":
                return "q"
            return Move(self, choice)
        else:
            return Move(self, random.randint(0, 2))

    def _move(self):
        while True:
            print(
                "\n".join(
                    [string.center(self.width) for string in Player.PROMPT]
                ),
            )
            player_choice = input("\n" + " " * (self.width // 2))
            if self._is_valid(player_choice) == "q":
                return "q"
            elif self._is_valid(player_choice):
                return int(player_choice) - 1
            else:
                print(
                    "\n".join(
                        [
                            string.center(self.width)
                            for string in Player.INVALID
                        ]
                    )
                )

    def _is_valid(self, choice: str):
        if not choice.isdigit():
            return "q" if choice.casefold() == "q" else False
        return True if int(choice) in [1, 2, 3] else False


class Move:
    MOVES = ["Rock", "Paper", "Scissors"]
    A_BEATS_B = [
        ["Rock", "Scissors"],
        ["Paper", "Rock"],
        ["Scissors", "Paper"],
    ]

    def __init__(self, player, choice: int):
        self.player = player
        self.move = Move.MOVES[choice]

    def __eq__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        return self.move == other.move

    def __lt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        return [other.move, self.move] in Move.A_BEATS_B


class RPSGame(ConsoleMixin):
    WELCOME = ["Welcome to Rock - Paper - Scissors!", "\n"]
    GOODBYE = ["", "Thanks for playing Rock - Paper - Scissors!", "Goodbye!"]
    BEATS = ["{0} beats {1}."]
    NO_BEATS = ["You both chose {0}."]
    WIN = ["You win!"]
    LOSE = ["You lose."]
    TIE = ["It's a tie."]

    def __init__(self):
        self._human = Player("human")
        self._computer = Player("computer")

    def _display_welcome_message(self):
        print(
            "".join([string.center(self.width) for string in RPSGame.WELCOME])
        )
        print("\n".join([string.center(self.width) for string in Rules.RULES]))

    def _display_goodbye_message(self):
        print(
            "\n".join(
                [string.center(self.width) for string in RPSGame.GOODBYE]
            )
        )

    def play(self):
        self._display_welcome_message()

        human_move = self._human.choose()
        if human_move == "q":
            self._display_goodbye_message()
            return
        computer_move = self._computer.choose()

        results = self._compare(human_move, computer_move)
        self._display_winner(results)

        self._display_goodbye_message()

    def _compare(self, move1: Move, move2: Move):
        if move1 == move2:
            return [move1]
        else:
            return sorted([move1, move2], reverse=True)

    def _display_winner(self, results):
        if len(results) == 1:
            no_beats = (
                RPSGame.NO_BEATS[0]
                .format(results[0].move.lower())
                .center(self.width)
            )
            print(f"\n{no_beats}\n")
            print(
                "\n".join(
                    [string.center(self.width) for string in RPSGame.TIE]
                )
            )
        else:
            beats = (
                RPSGame.BEATS[0]
                .format(results[0].move, results[1].move.lower())
                .center(self.width)
            )
            print(f"\n{beats}\n")
            if results[0].player.player_type == "human":
                print(
                    "\n".join(
                        [string.center(self.width) for string in RPSGame.WIN]
                    )
                )
            else:
                print(
                    "\n".join(
                        [string.center(self.width) for string in RPSGame.LOSE]
                    )
                )


new_game = RPSGame()
new_game.play()


"""
# Ties
moves = sorted([Move(Player("human"), 0), Move(Player("computer"), 0)])  # R, R
print([playermove.move for playermove in moves])

moves = sorted([Move(Player("human"), 1), Move(Player("computer"), 1)])  # P, P
print([playermove.move for playermove in moves])

moves = sorted([Move(Player("human"), 2), Move(Player("computer"), 2)])  # S, S
print([playermove.move for playermove in moves])


# Rock, Paper
moves = sorted([Move(Player("human"), 0), Move(Player("computer"), 1)])  # R, P
print([playermove.move for playermove in moves])

moves = sorted([Move(Player("human"), 1), Move(Player("computer"), 0)])  # R, P
print([playermove.move for playermove in moves])


# Paper, Scissors
moves = sorted([Move(Player("human"), 1), Move(Player("computer"), 2)])  # P, S
print([playermove.move for playermove in moves])

moves = sorted([Move(Player("human"), 2), Move(Player("computer"), 1)])  # P, S
print([playermove.move for playermove in moves])


# Scissors, Rock
moves = sorted([Move(Player("human"), 0), Move(Player("computer"), 2)])  # S, R
print([playermove.move for playermove in moves])

moves = sorted([Move(Player("human"), 2), Move(Player("computer"), 0)])  # S, R
print([playermove.move for playermove in moves])
"""
