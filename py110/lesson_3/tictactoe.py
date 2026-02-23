import os
import sys
import random

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
additional options to code:
    winning boards should be displayed with a line through the winning pattern
"""

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


def set_mode(state=None):
    print("  Please set the difficulty mode (1 - 4):\n")
    print("1. Easy    2. Medium    3. Hard    4. Human\n")

    difficulty = None
    while difficulty is None:
        difficulty = input()
        if len(difficulty) > 1 or difficulty not in "1234q":
            difficulty = None
            print("\n  Please select a choice from 1 to 4.\n")

    if difficulty.casefold() == "q":
        _ = os.system("clear")
        if state:
            display_board(state)
        print("\nThanks for playing!\n")
        sys.exit(0)

    return int(difficulty)


def change_mode(difficulty, state):
    print("\nWould you like to change the difficulty mode? (y/n)\n")
    change = False
    while change == False:
        change = input()
        if len(change) > 1 or change.casefold() not in "ynq":
            change = False
            print("\nPlease enter y or n\n")

    match change.casefold():
        case "y":
            display_board(state)
            print("")
            difficulty = set_mode(state)
        case "n":
            pass
        case "q":
            _ = os.system("clear")
            display_board(state)
            print("\nThanks for playing!\n")
            sys.exit(0)

    return difficulty


def new_board():
    return [" " for _ in range(9)]


def display_board(state):
    board_strings = [
        "     |     |",
        "_____|_____|_____",
        f"  {state[0]}  |  {state[1]}  |  {state[2]}",
        f"  {state[3]}  |  {state[4]}  |  {state[5]}",
        f"  {state[6]}  |  {state[7]}  |  {state[8]}",
    ]

    _ = os.system("clear")

    print("Enter 'q' at any time to quit.\n")

    for board_row in range(1, 10):
        match board_row:
            case a if a in [1, 4, 7, 9]:
                print(board_strings[0])
            case b if b in [3, 6]:
                print(board_strings[1])
            case 2:
                print(board_strings[2])
            case 5:
                print(board_strings[3])
            case 8:
                print(board_strings[4])


def first_player():
    print("\nWould you like to go first? (y/n)\n")
    first = None
    while first is None:
        first = input()
        if len(first) > 1 or first.casefold() not in "ynq":
            first = None
            print("\n  Please enter y or n.\n")

    match first.casefold():
        case "y":
            first = True
        case "n":
            first = False
        case "q":
            _ = os.system("clear")
            print("Thanks for playing!\n")
            sys.exit(0)

    return first


def user_X_or_O():
    print("\nDo you want to play X's or O's? (1-2 or X/O)\n")
    print("1. X\t\t2. O\n")

    while True:
        choice = input()
        if choice.casefold() not in "12xoq":
            print("\n  Please enter 1, 2, X, or O.\n")
        elif choice.casefold() == "q":
            _ = os.system("clear")
            print("Thanks for playing!\n")
            sys.exit(0)
        else:
            break

    if choice.casefold() in "1x":
        return ["X", "O"]
    else:
        return ["O", "X"]


def display_choices(state):
    for idx, value in enumerate(state):
        if value == " ":
            print(f"{idx + 1}. {DESCRIPTIONS[idx]}", end="")
        else:
            print(" " * (len(DESCRIPTIONS[idx]) + 3), end="")

        if (idx + 1) % 3 == 0:
            print("\n")
        else:
            print("\t", end="")


def user_turn(state, user_mark):
    choice_nums = [str(num) for num in range(1, 10) if state[num - 1] == " "]

    print(
        "\nYour Turn! Choose a square number to mark from the available selections below (1-9):\n"
    )
    while True:
        display_choices(state)
        choice = input()
        if choice.casefold() == "q":
            _ = os.system("clear")
            display_board(state)
            print("\nThanks for playing!\n")
            sys.exit(0)
        if choice in choice_nums:
            break
        display_board(state)
        print(
            "\nPlease choose a valid square number to mark from the available selections below (1-9):\n"
        )

    state[int(choice) - 1] = user_mark


def computer_turn(state, mode, user_char, comp_char):
    best_choices = set()
    # if a winning move is possible, make it (modes 1, 2, 3, 4)
    for idx_list in WIN_STATES:
        line = [state[idx_list[0]], state[idx_list[1]], state[idx_list[2]]]
        if line.count(comp_char) == 2 and line.count(" ") == 1:
            blank_space = idx_list[line.index(" ")]
            best_choices.add(blank_space)

    # otherwise, if user can make a winning move, block it (modes 3 and 4)
    if best_choices == set() and mode in [3, 4]:
        for idx_list in WIN_STATES:
            line = [state[idx_list[0]], state[idx_list[1]], state[idx_list[2]]]
            if line.count(user_char) == 2 and line.count(" ") == 1:
                blank_space = idx_list[line.index(" ")]
                best_choices.add(blank_space)

    # othwerise, if there are rows, columns, or diagonals with 1 X and 2 blanks, mark one of those blanks (modes 2, 3, 4)
    if best_choices == set() and mode in [2, 3, 4]:
        for idx_list in WIN_STATES:
            line = [state[idx_list[0]], state[idx_list[1]], state[idx_list[2]]]
            if line.count(comp_char) == 1 and line.count(" ") == 2:
                blank_space1 = idx_list[line.index(" ")]
                blank_space2 = idx_list[line.index(" ", line.index(" ") + 1)]
                for blank_space in [blank_space1, blank_space2]:
                    best_choices.add(blank_space)

    # otherwise, if there are rows, columns, or diagonals with 1 O and 2 blanks, mark one of those blanks (mode 4)
    if best_choices == set() and mode == 4:
        for idx_list in WIN_STATES:
            line = [state[idx_list[0]], state[idx_list[1]], state[idx_list[2]]]
            if line.count(user_char) == 1 and line.count(" ") == 2:
                blank_space1 = idx_list[line.index(" ")]
                blank_space2 = idx_list[line.index(" ", line.index(" ") + 1)]
                for blank_space in [blank_space1, blank_space2]:
                    best_choices.add(blank_space)

    # otherwise, any blank square is fair game (modes 1, 2, 3, 4)
    if best_choices == set():
        best_choices = [idx for idx, elem in enumerate(state) if elem == " "]

    best_choices = list(best_choices)
    chosen_idx = best_choices.pop(random.randint(0, len(best_choices) - 1))
    state[chosen_idx] = comp_char


def win_or_tie(state, user_char, comp_char):
    result = None
    for pattern in WIN_STATES:
        pattern_values = state[pattern[0]] + state[pattern[1]] + state[pattern[2]]

        if pattern_values == user_char * 3:
            result = "\nYou win!\n"
        elif pattern_values == comp_char * 3:
            result = "\nThe computer wins!\n"

    if result is None and " " not in state:
        result = "\nIt's a tie!\n"

    return result


def play_again(state):
    print("Would you like to play again? (y/n)\n")
    replay = None
    while replay is None:
        replay = input()
        if len(replay) > 1 or replay.casefold() not in "ynq":
            replay = None
            print("\nPlease enter y or n\n")

    match replay.casefold():
        case "y":
            replay = True
        case "n":
            replay = False
        case "q":
            _ = os.system("clear")
            display_board(state)
            print("\nThanks for playing!\n")
            sys.exit(0)

    return replay


def tictactoe():
    _ = os.system("clear")

    board = None
    difficulty = None

    while True:
        if board:
            display_board(board)

        if difficulty is None:
            print("\t\t  Welcome to Tic-Tac-Toe!!\n\t\t\t  By Adhish Yajnik\n")
            print("\t   Enter 'q' at any time to quit.\n")
            difficulty = set_mode()
        else:
            difficulty = change_mode(difficulty, board)

        is_user_turn = first_player()
        if not board:
            player_mark, computer_mark = user_X_or_O()
        board = new_board()
        display_board(board)

        random.seed()

        game_over = False

        # alternate between user and computer turns
        # and check for game-over each time a square is marked
        while not game_over:
            if is_user_turn:
                user_turn(board, player_mark)
            else:
                computer_turn(board, difficulty, player_mark, computer_mark)

            display_board(board)
            game_over = win_or_tie(board, player_mark, computer_mark)

            is_user_turn = not is_user_turn

        print(win_or_tie(board, player_mark, computer_mark))
        if play_again(board) == False:
            break

    _ = os.system("clear")
    display_board(board)
    print("\nThanks for playing!\n")


tictactoe()
