import random

VALID_CHOICES = {
    'r' : 'rock',
    'p' : 'paper',
    's' : 'scissors',
    'l' : 'lizard',
    'v' : 'spock',
}

LOSES_AGAINST = {
    'r' : (VALID_CHOICES['s'], VALID_CHOICES['l']),
    'p' : (VALID_CHOICES['r'], VALID_CHOICES['v']),
    's' : (VALID_CHOICES['p'], VALID_CHOICES['l']),
    'l' : (VALID_CHOICES['p'], VALID_CHOICES['v']),
    'v' : (VALID_CHOICES['r'], VALID_CHOICES['s']),
}

OUTCOMES = ["You win!\n",
            "Computer wins!\n",
            "It's a tie!\n"]

def prompt(message):
    print(f"==> {message}")

def get_choice():
    print()
    prompt('Choose one:')

    choices_zipped = list(zip(VALID_CHOICES,
                              VALID_CHOICES.values()))
    for elem1, elem2 in choices_zipped:
        prompt(f'  {elem1}\t({elem2})')
    print()

    choice = input()
    while not (choice in VALID_CHOICES or
                choice in VALID_CHOICES.values()):
        prompt("That's not a valid choice\n")
        choice = input()

    if choice not in VALID_CHOICES.values():
        choice = VALID_CHOICES[choice]

    return choice

def compute_winner(player, comp):
    print()
    prompt(f'USER: {player.title()} - COMPUTER: {comp.title()}')

    player_key = [key for key, value in VALID_CHOICES.items() if value == player][0]

    if comp in LOSES_AGAINST[player_key]:
        outcome = 0 # user wins
    elif player == comp:
        outcome = 2 # tie
    else:
        outcome = 1 # computer wins
    return OUTCOMES[outcome]

def update_score(winner_of_round):
    if winner_of_round == OUTCOMES[0]:
        score[0] += 1
    elif winner_of_round == OUTCOMES[1]:
        score[1] += 1

def print_score():
    prompt(f'***SCORE*** <==\n'
           f'USER: {score[0]} - COMPUTER: {score[1]}\n')

def play_again():
    prompt('Play again -- best of 5?\n')

    response = input().lower()
    while not (response.startswith('n') or response.startswith('y')):
        print()
        prompt("That's not a valid choice\n")
        response = input().lower()

    return response

def print_overall_winner():
    if score[0] == 3:
        prompt('You win best of 5!\n')
    elif score[1] == 3:
        prompt('Computer wins best of 5!\n')
    print_score()

score = [0, 0]

while True:
    user_choice = get_choice()

    computer_choice = random.choice(list(VALID_CHOICES.values()))

    WINNER = compute_winner(user_choice, computer_choice)

    prompt(WINNER)

    update_score(WINNER)

    if 3 not in score:
        print_score()

        answer = play_again()
        if answer.startswith('n'):
            break
    else:
        print_overall_winner()
        break