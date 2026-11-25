import random


class Player:
    CHOICES = ("rock", "paper", "scissors")

    def __init__(self):
        self.move = None


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt_lines = [
            "Choose a move and press Enter:",
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
        self.move = random.choice(Player.CHOICES)


class RPSGame:
    A_BEATS_B = (
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    )

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

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
            print("You win!")
        else:
            print("Computer wins!")

    def _play_again(self):
        prompt_lines = [
            "Would you like to play again? (y/n)",
            "> ",
        ]
        prompt = "\n".join(prompt_lines)

        while True:
            answer = input(prompt).strip().lower()
            if answer[0] in "yn":
                return answer.startswith("y")

            print(f"{answer} is invalid")

    def play(self):
        while True:
            self._display_welcome_message()
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()


game = RPSGame()
game.play()
