import os
import sys
import random
import re

"""
High-level Algorithm:

1. Display the empty 3x3 board
2. Ask the user to mark a square
3. Display the updated board
4. If it's a winning board, display the winner and go to step 9
5. If the board is full, display tie and go to step 9
6. If neither player won and the board is not full, then move on:
7. The computer marks a square
8. Repeat steps 3-6
9. Ask user if they want to play again
10. If yes, return to step 1
11. Print a goodbye message for the user

Sub algorithms:
- Display the empty 3x3 board / display the updated board
- Ask the user to mark a square
- Check for a winning or tie board and skip ahead if it is
- Computer marks a square
- Ask the user if they want to play again and loop to beginning if so
- Print goodbye message


=====


Display the empty 3x3 board / display the updated board:

     |     |
  X  |  O  |  X
_____|_____|_____
     |     |
  X  |  O  |  X
_____|_____|_____
     |     |
  X  |  O  |  X
     |     |

Print strings representing each text row in the above format
    Rows 1, 4, 7, and 9:    '     |     |'
    Rows 3 and 6:           '_____|_____|_____'
    Row 2:                  f'  {state[0][0]}  |  {state[0][1]}  |  {state[0][2]}',
    Row 5:                  f'  {state[1][0]}  |  {state[1][1]}  |  {state[1][2]}',
    Row 8:                  f'  {state[2][0]}  |  {state[2][1]}  |  {state[2][2]}',

We can store each of these strings in a list: board_strings

We can pull the values for top_left, top_center, top_right, etc. from nested lists of strings,
whose values are either ' ', 'X', or 'O':

state = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

We can print the board by looping through a range from 1-9 (meaning range(1, 10)) and selecting which string to print based on the iteration number.
    - Use a match case construction for this:
    - if the iteration number is 1, 4, 7, or 9, print board_strings[0]
    - if the iteration number is 3 or 6, print board_strings[1]
    - if the iteration number is 2, print board_strings[2]
    - if the iteration number is 5, print board_strings[3]
    - if the iteration number is 8, print board_strings[4]


=====


Ask the user to mark a square:

We want to print a string that prompts the user and also displays their choices in a grid
that corresponds to the board itself:

1. Upper Left   2. Upper Center     3. Upper Right

4. Center Left  5. Center Center    6. Center Right

7. Bottom Left  8. Bottom Center    9. Bottom Right

If a space on the board has already been marked, we want to replace it with an empty space in the choices grid

1. Upper Left   2. Upper Center     3. Upper Right

                5. Center Center    6. Center Right

7. Bottom Left  8. Bottom Center    9. Bottom Right

The user should input a number from 1 to 9 to make their selection

If the number is not valid, the user should be asked to make a valid selection and the choices grid displayed again

The function should then update board_state with the selection and return it so that it can be used later

Inputs: nested lists of available choices (board_state)

Algorithm:
- flatten board_state and assign it to available_choices --> [" ", " ", " ", " ", " ", " ", " ", " ", " "]
- initialize a descriptions list to ['Upper Left', 'Upper Center', 'Upper Right'...]
- print a message asking the user to make a selection from the available choices below
- iterate through each index, element in enumerated available_choices:
    - if the element is " ", print an f-string: the index + 1, followed by a period, space, and descriptions[index], omitting the trailing line break
    - otherwise, print a single space character multiplied by the length of descriptions[index] + 3, omitting the trailing line break
    - if index + 1 is divisible by 3, print a newline character
    - otherwise, print a tab character, omitting the trailing line break
- prompt the user to make a selection from 1 to 9, excluding choices that are not listed
- if the user's choice is invalid, prompt them to make a valid selection and print the available choices again.


=====


Computer marks a square

Inputs: board_state

Algorithm:
- flatten board_state and assign it to available_choices --> [" ", " ", " ", " ", " ", " ", " ", " ", " "]
- initialize a win_states list to [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
- initialize a best_choices set to an empty set
- Start a while True loop:
    - iterate through each idx_list in win_states:
        - initialize line = [available_list[idx_list[0]], available_list[idx_list[1]], available_list[idx_list[2]]]
        - if line has 2 X's and 1 blank:
            - initialize blank_space to the index of the blank space in line
            - add idx_list[blank_space] to best_choices
    - if best_choices is not empty, break
    - iterate through each idx_list in win_states:
        - initialize line = [available_list[idx_list[0]], available_list[idx_list[1]], available_list[idx_list[2]]]
        - if line has 2 O's and 1 blank:
            - initialize blank_space to the index of the blank space in line
            - add idx_list[blank_space] to best_choices
    - if best_choices is not empty, break
    - iterate through each idx_list in win_states:
        - initialize line = [available_list[idx_list[0]], available_list[idx_list[1]], available_list[idx_list[2]]]
        - if line has 1 X and 2 blanks:
            - initialize blank_space1 to the index of the first blank space in line
            - initialize blank_space2 to the index of the next blank space in line (set the second argument of list.index to blank_space1 + 1 so the search begins from there)
            - add idx_list[blank_space1] and idx_list[blank_space2] to best_choices
    - if best_choices is not empty, break
    - iterate through each idx_list in win_states:
        - initialize line = [available_list[idx_list[0]], available_list[idx_list[1]], available_list[idx_list[2]]]
        - if line has 1 O and 2 blanks:
            - initialize blank_space1 to the index of the first blank space in line
            - initialize blank_space2 to the index of the next blank space in line (set the second argument of list.index to blank_space1 so the search begins from there)
            - add idx_list[blank_space1] and idx_list[blank_space2] to best_choices
    - if best_choices is not empty, break
    - iterate through each index and element in enumerated available_choices:
        - if the element is ' ':
            - add its index to best_choices

- pop a random member out of the best_choices set and assign it to chosen_idx
- in available_choices, assign the element at chosen_idx to X
- generate a new nested board_state list from available_choices and return it
"""

"""
updates:
+ rename functions more clearly:
    set_mode() --> prompt_difficulty_mode()
    change_mode() --> prompt_mode_change()
    first_player() --> prompt_turn_order()
    user_X_or_O() --> prompt_user_symbol()
    play_again() --> prompt_play_again
    win_or_tie() --> get_game_result()

rename variables more clearly:
    - consider changing state to board
    + blank_space1 and blank_space2 in computer_turn() could be more descriptive
    
* define constants BOARD_SIZE = 9 and GRID_SIZE = 3 and reference those later to avoid magic numbers later in the code
+ no need to call random.seed() before each new game(?)
+ when displaying game end result message, make user press enter before asking if they want to play again
+ remove overuse of match-case constructions; replace with simple if-elifs. See display_board() for an example.

+ add comment to explain the formatting choice logic in display_choices()
+ add rules explanation to the welcome message
+ add descriptions to the difficulty modes

- fill blank spaces on the board with numbers 1-9 instead of spaces

+ don't use sys.exit(0) to exit when user enters 'q'. Use a specific return value and have the main loop check for that

- remove duplicate logic
    + generic prompt_user() function whose user prompting and validation structure can be reused throughout the program
    - generic find_best_moves() function whose structure can be reused throughout the computer_turn() function
    + generic clear_screen() function that can be reused throughout the program
"""

WELCOME_MESSAGE = """
Welcome to Tic-Tac-Toe!!
Programmed by Adhish Yajnik

The user and the computer take turns marking squares on a 3x3 grid, 'X' and
'O.' The first player to mark 3 squares in a row with their symbol wins
(horizontally, vertically, or diagonally)."""

GREETING_PROMPT = """Press Enter to continue.
Enter 'q' at any time to quit."""

NON_QUIT_INPUTS = "".join([chr(i) for i in range(128) if chr(i) not in "Qq"])

DIFFICULTY_DESCRIPTIONS = """
Please set the difficulty mode (1 - 4):

1. EASY - the computer marks squares at random, unless it has a winning move 
   available                                                                 

2. MEDIUM - the computer avoids marking squares if they won't contribute to a
   complete row                                                              

3. HARD - the computer always tries to block a winning move available to the 
   user                                                                      

4. MASTER - the computer blocks the user from even starting a row, wherever  
   possible                                                                  """

USER_CHARACTER_PROMPT = """
Do you want to play X's or O's? (1, 2, X, or O)

1. X    2. O"""

GRID_SIZE, BOARD_SIZE = 3, 9

CONSOLE_SIZE = 79

WIN_STATES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

DESCRIPTIONS = (
    "Upper Left   ",
    "Upper Center ",
    "Upper Right",
    "Middle Left  ",
    "Middle Center",
    "Middle Right",
    "Bottom Left  ",
    "Bottom Center",
    "Bottom Right",
)

DESC_MAX = 16


def clear_screen():
    _ = os.system("clear")


def center_text(input_string, end="\n"):
    lines = input_string.split("\n")
    centered = ""
    for line in lines:
        centered += line.center(CONSOLE_SIZE) + end

    return centered


def prompt_user(message, valid_inputs, error_message="Invalid input\n"):
    print(center_text(message))
    while True:
        user_input = input().strip().casefold()
        if user_input == "q":
            return "quit"
        if user_input in valid_inputs:
            return user_input
        print(center_text(error_message))


def prompt_difficulty_mode():
    error_message = "\nPlease select a choice from 1 to 4."

    difficulty = prompt_user(DIFFICULTY_DESCRIPTIONS, "1234", error_message)

    return difficulty


def prompt_mode_change(state, difficulty, player_1, user_char, comp_char):
    prompt_message = "\nWould you like to change the difficulty mode? (y/n)"
    error_message = "\n  Please enter y or n"

    change = prompt_user(prompt_message, "yn", error_message)

    match change:
        case "y":
            display_board(state, difficulty, player_1, user_char, comp_char)
            print("")
            difficulty = prompt_difficulty_mode()
        case "n":
            pass
        case "q":
            return "quit"

    return difficulty


def new_board():
    return [str(num + 1) for num in range(BOARD_SIZE)]


def display_board(state, difficulty, user_goes_first, user_char="O", comp_char="X"):
    # this function prints one of these five strings
    # in order to draw the tic-tac-toe board:
    #      |     |
    #      |     |
    # _____|_____|_____
    #      |     |
    #      |     |
    # _____|_____|_____
    #      |     |
    #      |     |
    #      |     |
    board_strings = [
        center_text("     |     |     "),
        center_text("_____|_____|_____"),
        center_text(f"  {state[0]}  |  {state[1]}  |  {state[2]}  "),
        center_text(f"  {state[3]}  |  {state[4]}  |  {state[5]}  "),
        center_text(f"  {state[6]}  |  {state[7]}  |  {state[8]}  "),
    ]

    levels = {1: "EASY", 2: "MEDIUM", 3: "HARD", 4: "MASTER"}

    clear_screen()

    if user_goes_first:
        status_line = f"USER: {user_char}    COMPUTER: {comp_char}    DIFFICULTY: {levels[int(difficulty)]}"
    else:
        status_line = f"COMPUTER: {comp_char}    USER: {user_char}    DIFFICULTY: {levels[int(difficulty)]}"

    print(center_text("Enter 'q' at any time to quit."))
    print(center_text(status_line))

    # depending on the row of the tic-tac-toe ascii drawing
    # draw one of the five strings above
    for board_row in range(1, 10):
        if board_row in [1, 4, 7, 9]:
            print(board_strings[0], end="")
        elif board_row in [3, 6]:
            print(board_strings[1], end="")
        elif board_row == 2:
            print(board_strings[2], end="")
        elif board_row == 5:
            print(board_strings[3], end="")
        elif board_row == 8:
            print(board_strings[4], end="")


def prompt_turn_order(state, difficulty, player_1, user_char, comp_char):
    prompt_message = "\nWould you like to go first? (y/n)"
    error_message = "\nPlease enter y or n."

    if state:
        display_board(state, difficulty, player_1, user_char, comp_char)
    else:
        clear_screen()
    user_first = prompt_user(prompt_message, "yn", error_message)

    match user_first:
        case "y":
            return True
        case "n":
            return False
        case "quit":
            return "quit"


def prompt_user_symbol():
    error_message = "\nPlease enter 1, 2, X, or O."

    clear_screen()
    user_char = prompt_user(USER_CHARACTER_PROMPT, "12xo", error_message)

    if user_char == "quit":
        return "quit"
    elif user_char in "1x":
        return ["X", "O"]
    else:
        return ["O", "X"]


def display_choices(state):
    cur_line = []
    for idx, value in enumerate(state):
        if value.isnumeric():
            cur_line.append(f"{idx + 1}. {DESCRIPTIONS[idx]}".ljust(DESC_MAX))
        else:
            cur_line.append(" " * (DESC_MAX))

        if (idx + 1) % GRID_SIZE == 0:
            print(center_text("    ".join(cur_line)))
            cur_line = []


def prompt_user_turn(state, difficulty, first_player, user_mark, comp_mark):
    choice_nums = [str(num) for num in range(1, 10) if state[num - 1].isnumeric()]

    print(
        "\nYour Turn! Choose a square number to mark from the available selections below (1-9):\n"
    )
    while True:
        display_choices(state)
        choice = input()
        if choice.casefold() == "q":
            return "quit"
        if choice in choice_nums:
            break
        display_board(state, difficulty, first_player, user_mark, comp_mark)
        print(
            "\nPlease choose a valid square number to mark from the available selections below (1-9):\n"
        )

    state[int(choice) - 1] = user_mark


def find_strategic_moves(state, character, required_num):
    moves = set()
    for idx_list in WIN_STATES:
        line = "".join([state[idx_list[0]], state[idx_list[1]], state[idx_list[2]]])
        if (line.count(character) == required_num) and (
            len(re.findall("[1-9]", line)) == (3 - required_num)
        ):
            for idx, val in enumerate(line):
                if val.isnumeric():
                    moves.add(idx_list[idx])

    return moves


def computer_turn(state, mode, user_char, comp_char):
    best_choices = set()
    # if a winning move is possible, make it (modes 1, 2, 3, 4)
    best_choices = find_strategic_moves(state, comp_char, 2)
    # otherwise, if user can make a winning move, block it (modes 3 and 4)
    if best_choices == set() and mode in [3, 4]:
        best_choices = find_strategic_moves(state, user_char, 2)
    # othwerise, if there are rows, columns, or diagonals with 1 X and 2 blanks, mark one of those blanks (modes 2, 3, 4)
    elif best_choices == set() and mode in [2, 3, 4]:
        best_choices = find_strategic_moves(state, comp_char, 1)
    # otherwise, if there are rows, columns, or diagonals with 1 O and 2 blanks, mark one of those blanks (mode 4)
    elif best_choices == set() and mode == 4:
        best_choices = find_strategic_moves(state, user_char, 1)
    elif best_choices == set():
        best_choices = [idx for idx, elem in enumerate(state) if elem.isnumeric()]

    best_choices = list(best_choices)
    chosen_idx = best_choices.pop(random.randint(0, len(best_choices) - 1))
    state[chosen_idx] = comp_char


def get_game_result(state, user_char, comp_char):
    for pattern in WIN_STATES:
        pattern_values = state[pattern[0]] + state[pattern[1]] + state[pattern[2]]

        if pattern_values == user_char * GRID_SIZE:
            return center_text("\nYou win!")
        elif pattern_values == comp_char * GRID_SIZE:
            return center_text("\nThe computer wins!")

    if not "".join(state).isalnum():
        return center_text("\nIt's a tie!")


def prompt_play_again():
    prompt_message = "Would you like to play again? (y/n)"
    error_message = "\nPlease enter y or n."

    replay = prompt_user(prompt_message, "yn", error_message)

    match replay:
        case "y":
            return True
        case "n":
            return False
        case "q":
            return "quit"


def tictactoe():
    clear_screen()

    board, difficulty, player_mark, computer_mark, first_player = [None] * 5

    while True:
        if board:
            display_board(board, difficulty, first_player, player_mark, computer_mark)

        if difficulty is None:
            print(center_text(WELCOME_MESSAGE))

            advance = prompt_user(GREETING_PROMPT, NON_QUIT_INPUTS)
            if advance == "quit":
                break

            clear_screen()
            difficulty = prompt_difficulty_mode()
        else:
            difficulty = prompt_mode_change(
                board, difficulty, first_player, player_mark, computer_mark
            )
        if difficulty == "quit":
            break

        if board:
            display_board(board, difficulty, first_player, player_mark, computer_mark)
        first_player = is_user_turn = prompt_turn_order(
            board, difficulty, first_player, player_mark, computer_mark
        )
        if is_user_turn == "quit":
            break
        if not board:
            symbols = prompt_user_symbol()
        if symbols == "quit":
            break
        player_mark, computer_mark = symbols
        board = new_board()
        display_board(board, difficulty, first_player, player_mark, computer_mark)

        # random.seed()

        game_over = False
        force_quit = False

        # alternate between user and computer turns
        # and check for game-over each time a square is marked
        while not game_over:
            if is_user_turn:
                if (
                    prompt_user_turn(
                        board, difficulty, first_player, player_mark, computer_mark
                    )
                    == "quit"
                ):
                    force_quit = True
                    break
            else:
                computer_turn(board, difficulty, player_mark, computer_mark)

            display_board(board, difficulty, first_player, player_mark, computer_mark)
            game_over = get_game_result(board, player_mark, computer_mark)

            is_user_turn = not is_user_turn

        if force_quit == True:
            break

        print(get_game_result(board, player_mark, computer_mark))
        print(center_text("Press enter to continue"))
        if input() in "Qq":
            break
        if prompt_play_again() in [False, "quit"]:
            break

    if board:
        display_board(board, difficulty, first_player, player_mark, computer_mark)
    print(center_text("\nThanks for playing!"))


tictactoe()
