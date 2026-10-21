import os
import random

# CONSTANTS
# Cards
SUITS = 4

FACE_CARDS = ["Jack", "Queen", "King"]

ACE = "Ace"

POINT_VALUES = (
    {str(num): num for num in range(2, 11)}
    | {card: 10 for card in FACE_CARDS}
    | {ACE: {"High": 11, "Low": 1}}
)

# Integers
BLACKJACK = 21

INITIAL_DEAL = 2

HIT_THRESHOLD = 17

# Strings
AN_NOUNS = ["8", "Ace"]

MODE_STR = r"""Would you like to play (1) H17 or (2) S17?

H17: The dealer hits if they have less than 17 points, or
     if they have 17 points by with an 11-point Ace in hand (a soft 17).

S17: The dealer stays if they have 17 points,
     whether it's a soft 17 or a hard 17."""

WELCOME_STR = r"""                      ___  __         __     _          __
                     / _ )/ /__ _____/ /__  (_)__ _____/ /__
                    / _  / / _ `/ __/  '_/ / / _ `/ __/  '_/
                   /____/_/\_,_/\__/_/\_\_/ /\_,_/\__/_/\_\
                                       |___/
                          Programmed by Adhish Yajnik
                         Enter (q) at any time to quit

Blackjack is a popular casino card game where players aim to beat the
dealer by having a hand total closer to 21 than the dealer's, without
exceeding 21 ("busting"). Players receive two cards and can "hit" (take
more) or "stay" (keep current total).

- Numbered cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10
- Aces are worth 1 or 11"""

MSGS = {
    "prompt_continue": "Press (enter) to continue or (q) to quit.",
    "prompt_mode": MODE_STR,
    "prompt_cash": "How much cash do you have to play with?",
    "prompt_bet": "How much do you want to bet on this hand?",
    "prompt_split": "Do you want to split your {} pair? (y) (n)",
    "prompt_ddown": "Do you want to double down? (y) (n)",
    "prompt_hit": "Do you want to (1) hit or (2) stay?",
    "prompt_repeat": "Do you want to play another hand? (y) (n)",
    "err_valid_num": "Please enter a positive whole number.",
    "err_choices": "Please enter a number from 1 to {}.",
    "err_y_n": "Please enter y or n only, or q to quit.",
    "err_limit": "Please enter a bet you can afford. (${} max)",
    "welcome": WELCOME_STR,
    "inital_wager": "You wagered ${} on this hand.",
    "header": "ROUND: {}    WAGER{}: {}{}    CASH: {}",
    "deck_shuffled": "The deck has been shuffled.",
    "wager_doubled": "Your wager doubled to ${}.",
    "player_draw": "You drew {} {}{}",
    "player_stay": "You stayed at {}.",
    "and_bust": " and went bust.",
    "money_won_lost": "{}You {} ${}",
    "bust_lost": "You lost ${}.",
    "dealer_turn": "It is the dealer's turn.",
    "dealer_draw": "The dealer drew {} {}{}",
    "dealer_stay": "The dealer stays.",
    "bust_won": "You won ${}.",
    "hole_card": "The dealer's hole card was {} {}",
    "won_lost": "{}{} won {} to {}{}",
    "push": "{}Push. No winner.",
    "blackjack": "{}{} won with a {}blackjack{}",
    "result": "{}You {} ${}",
    "cash_on_hand": "You have ${}.",
    "out_of_cash": "You're out of cash!",
    "thanks": "Thanks for playing!",
    "goodbye": "Goodbye!",
}


def prompt_continue() -> str:
    print(f"{MSGS['prompt_continue']}\n")
    user_input = input().strip().casefold()
    print()
    return user_input if user_input == "q" else ""


def prompt_dollars(pmt_msg: str, limit=float("inf")) -> int | str:
    print(f"{pmt_msg}\n")
    while True:
        user_input = input("$").strip()
        print()
        # is "q"
        if user_input == "q":
            return "q"

        err_msg = MSGS["err_valid_num"]
        # is integer greater than 0
        if (not user_input.isdigit()) or (int(user_input) <= 0):
            print(f"{err_msg}\n")
            continue
        user_num = int(user_input)

        # is less than or equal to limit
        err_limit = MSGS["err_limit"].format(limit)
        if user_num > limit:
            print(f"{err_limit}\n")
            continue
        return [user_num]


def prompt_choices(
    pmt_msg: str, num_choices: int, err_msg=MSGS["err_choices"]
) -> int | str:
    print(f"{pmt_msg}\n")
    while True:
        user_input = input().strip().casefold()
        print()
        if user_input.isdigit():
            if int(user_input) in range(1, num_choices + 1):
                return int(user_input)
        elif user_input == "q":
            return "q"
        print(err_msg.format(num_choices))
        print()


def prompt_y_n(pmt_msg: str) -> str:
    print(f"{pmt_msg}\n")
    while True:
        user_input = input().strip().casefold()
        print()
        if user_input in ("y", "n", "q"):
            return user_input
        print(f"{MSGS['err_y_n']}\n")


def prompt_cash() -> list | str:
    return prompt_dollars(MSGS["prompt_cash"])


def prompt_bet(cash: list) -> list | str:
    return prompt_dollars(MSGS["prompt_bet"], cash[0])


def prompt_mode() -> int:
    return prompt_choices(MSGS["prompt_mode"], 2)


def prompt_split(player_hands: list, bets: list) -> str:
    split = prompt_y_n(MSGS["prompt_split"].format(player_hands[0][0]))
    if split == "y":
        player_hands.append([player_hands[0].pop()])
        bets.append(bets[0])
    return split


def prompt_ddown() -> str:
    return prompt_y_n(MSGS["prompt_ddown"])


def prompt_repeat(game_stats: dict) -> str:
    reprint_hands(game_stats, reveal=True)
    return prompt_y_n(MSGS["prompt_repeat"])


def clear_screen() -> None:
    _ = os.system("clear")


def shuffle_deck() -> list:
    deck = ([str(num) for num in range(2, 11)] + FACE_CARDS + [ACE]) * 4
    random.shuffle(deck)
    return deck


def deal_cards(deck: list) -> list:
    player_hands = [[]]
    dealer_hands = [[]]
    for _ in range(INITIAL_DEAL):
        player_hands[0].append(deck.pop())
        dealer_hands[0].append(deck.pop())
    return [dealer_hands, player_hands]


def print_player_hands(hands: list, bets: list) -> None:
    actual_hands = [hand for hand in hands if hand]
    actual_bets = [bet for bet in bets if bet]
    for h_idx, hand in enumerate(actual_hands):
        cards = ""
        for c_idx, card in enumerate(hand):
            cards += card
            if c_idx != len(hand) - 1:
                cards += ", "
        cards = cards.ljust(30)
        prefix = "" if len(actual_hands) == 1 else f"Hand {h_idx + 1} "
        info = f"{prefix}(${actual_bets[h_idx]} wagered)"
        output = cards + info
        print(output)


def print_dealer_hands(hands: list, reveal: bool) -> None:
    output = ""
    if hands:
        for idx, card in enumerate(hands[0]):
            if reveal:
                output += card
            else:
                if idx != 1:
                    output += card
                else:
                    output += "hole card"
            if idx != len(hands[0]) - 1:
                output += ", "
    print(output)


def reprint_hands(game_stats: dict, reveal=False) -> None:
    actual_bets = [bet for bet in game_stats["bets"] if bet]
    if actual_bets:
        first_bet = f"${actual_bets[0]}"
        second_bet, plural = "", ""
        if len(actual_bets) > 1:
            second_bet = f", ${actual_bets[1]}"
            plural = "S"
    else:
        first_bet, second_bet, plural = "", "", ""
    clear_screen()
    print(f"ROUND: {game_stats['round_no'][0]}", end="")
    print(f"WAGER{plural}: {first_bet}{second_bet}".center(30), end="")
    print(f"CASH: ${game_stats['cash'][0]}")
    print()
    print("DEALER:")
    print_dealer_hands(game_stats["dealer_hands"], reveal)
    print()
    print("YOU:")
    print_player_hands(game_stats["player_hands"], game_stats["bets"])
    print()


def hit(hand, deck):
    hand.append(deck.pop())


def get_a_an(card: str) -> str:
    return "an" if card in AN_NOUNS else "a"


def calc_points2(hand: list) -> float | int:
    points = sum([POINT_VALUES[card] for card in hand if card != ACE])

    # add Aces valued 11 if they don't cause a bust, otherwise 1
    for ace in [card for card in hand if card == ACE]:
        if points + POINT_VALUES[ace]["High"] <= BLACKJACK:
            points += POINT_VALUES[ace]["High"]
            points = float(points)  # soft hands are floats
        else:
            points += POINT_VALUES[ace]["Low"]  # hard hands are ints

    # float if soft, integer if hard
    return points


def is_bust(hand: list) -> bool:
    return calc_points2(hand) > BLACKJACK


def remove_empty_lists(lst: list) -> None:
    while [] in lst:
        lst.remove([])


def double_down2(idx: int, game_stats: dict) -> str:
    game_stats["bets"][idx] *= 2
    reprint_hands(game_stats)
    print(MSGS["wager_doubled"].format(game_stats["bets"][idx]))
    print()

    if prompt_continue() == "q":
        return "q"

    hit(game_stats["player_hands"][idx], game_stats["deck"])
    bust = is_bust(game_stats["player_hands"][idx])
    end_str = MSGS["and_bust"] if bust else "."

    reprint_hands(game_stats)
    drawn_card = game_stats["player_hands"][idx][-1]
    print(
        MSGS["player_draw"].format(get_a_an(drawn_card), drawn_card, end_str)
    )
    print()

    if prompt_continue() == "q":
        return "q"

    if bust:
        game_stats["cash"][0] -= game_stats["bets"][idx]
        output_str = MSGS["bust_lost"].format(game_stats["bets"][idx]) + "\n"
        reprint_hands(game_stats)
        print(output_str)

        if prompt_continue() == "q":
            return "q"

        output_str += (
            "\n" + MSGS["cash_on_hand"].format(game_stats["cash"][0]) + "\n"
        )
        reprint_hands(game_stats)
        print(output_str)

        if prompt_continue() == "q":
            return "q"

        game_stats["player_hands"][idx].clear()
        game_stats["bets"][idx] = ""
    return ""


def hit_or_stay2(idx: int, game_stats: dict) -> str:
    while True:
        reprint_hands(game_stats)
        choice = prompt_choices(MSGS["prompt_hit"], 2)
        if choice == "q":
            return "q"
        # user stays
        if choice == 2:
            reprint_hands(game_stats)
            points = int(calc_points2(game_stats["player_hands"][idx]))
            print(MSGS["player_stay"].format(points))
            print()
            if prompt_continue() == "q":
                return "q"
            break
        # user hits
        if choice == 1:
            hit(game_stats["player_hands"][idx], game_stats["deck"])
            bust = is_bust(game_stats["player_hands"][idx])
            end_str = MSGS["and_bust"] if bust else "."

            reprint_hands(game_stats)
            drawn_card = game_stats["player_hands"][idx][-1]
            print(
                MSGS["player_draw"].format(
                    get_a_an(drawn_card), drawn_card, end_str
                )
            )
            print()

            if prompt_continue() == "q":
                return "q"

            if bust:
                game_stats["cash"][0] -= game_stats["bets"][idx]
                output_str = (
                    MSGS["bust_lost"].format(game_stats["bets"][idx]) + "\n"
                )
                reprint_hands(game_stats)
                print(output_str)

                if prompt_continue() == "q":
                    return "q"

                output_str += (
                    "\n"
                    + MSGS["cash_on_hand"].format(game_stats["cash"][0])
                    + "\n"
                )
                reprint_hands(game_stats)
                print(output_str)

                if prompt_continue() == "q":
                    return "q"

                game_stats["player_hands"][idx].clear()
                game_stats["bets"][idx] = ""
                break
    return ""


def player_turn2(game_stats: dict) -> str:
    for idx, hand in enumerate(game_stats["player_hands"]):
        if len(hand) < 2:
            hit(hand, game_stats["deck"])
        reprint_hands(game_stats)
        ddown = prompt_ddown()
        if ddown == "q":
            return "q"
        if ddown == "y":
            if double_down2(idx, game_stats) == "q":
                return "q"
        else:
            if hit_or_stay2(idx, game_stats) == "q":
                return "q"
        return ""


def dealer_turn(game_stats: dict, mode: int) -> str:
    reprint_hands(game_stats)

    print(MSGS["dealer_turn"])
    print()

    if prompt_continue() == "q":
        return "q"

    # mode 1 is H17, mode 2 is S17
    while True:
        reprint_hands(game_stats)
        points = calc_points2(game_stats["dealer_hands"][0])

        draw = False
        if points < HIT_THRESHOLD:
            draw = True
        if mode == 1:  # if mode is H17
            if points == HIT_THRESHOLD and isinstance(
                points, float
            ):  # if hand is soft 17
                draw = True

        if draw:
            hit(game_stats["dealer_hands"][0], game_stats["deck"])
            bust = is_bust(game_stats["dealer_hands"][0])
            end_str = MSGS["and_bust"] if bust else "."

            reprint_hands(game_stats)
            drawn_card = game_stats["dealer_hands"][0][-1]
            print(
                MSGS["dealer_draw"].format(
                    get_a_an(drawn_card), drawn_card, end_str
                )
            )
            print()

            if prompt_continue() == "q":
                return "q"

            if bust:
                total_bets = sum(game_stats["bets"])
                game_stats["cash"][0] += total_bets
                output_str = MSGS["bust_won"].format(total_bets) + "\n"
                reprint_hands(game_stats)
                print(output_str)

                if prompt_continue() == "q":
                    return "q"

                output_str += (
                    "\n"
                    + MSGS["cash_on_hand"].format(game_stats["cash"][0])
                    + "\n"
                )
                reprint_hands(game_stats)
                print(output_str)

                if prompt_continue() == "q":
                    return "q"

                game_stats["dealer_hands"][0].clear()
                break
        else:
            reprint_hands(game_stats)
            print(MSGS["dealer_stay"])
            print()

            if prompt_continue() == "q":
                return "q"
            break
    return ""


def reveal_hole_card(game_stats: dict) -> None:
    hole_card = game_stats["dealer_hands"][0][1]
    print(MSGS["hole_card"].format(get_a_an(hole_card), hole_card))
    print()


def get_winner(p_hand_idx: int, game_stats: dict) -> int | float:
    player_hand = game_stats["player_hands"][p_hand_idx]
    dealer_hand = game_stats["dealer_hands"][0]

    points = [calc_points2(player_hand), calc_points2(dealer_hand)]
    cards = [len(player_hand), len(dealer_hand)]

    result_sign = [1, -1]
    win_type = 0

    # if hands are tied
    if len(set(points)) == 1:
        # if hands are the same length
        if len(set(cards)) == 1:
            win_type = idx = 0
        # if one player has a natural blackjack
        elif BLACKJACK in points and INITIAL_DEAL in cards:
            idx = cards.index(INITIAL_DEAL)
            win_type = 2.0
        # if hands are different lengths without a natural blackjack
        else:
            win_type = idx = 0
    # if hands are not tied
    else:
        idx = points.index(max(points))
        # if the winner has a blackjack
        if max(points) == BLACKJACK:
            # if the winner has a natural blackjack
            if cards[idx] == INITIAL_DEAL:
                win_type = 2.0
            # if the winner has a regular blackjack
            else:
                win_type = 1.0
        # if the winner doesn't have a blackjack
        else:
            win_type = 1

    # multiply the sign (+1 or -1) by the win type (0, 1, 1.0, or 2.0)
    return result_sign[idx] * win_type


def print_results(results: list, game_stats: dict) -> str:
    dealer_pts = calc_points2(game_stats["dealer_hands"][0])

    result_str = ""

    for idx, multiplier in enumerate(results):
        hand_no = f"Hand {idx + 1}: " if len(results) > 1 else ""

        reprint_hands(game_stats, reveal=True)

        if multiplier == 0:
            result_str += ("\n" * idx) + MSGS["push"].format(hand_no) + "\n"
            print(result_str)
            if prompt_continue():
                return "q"
            continue

        who_won, end_str = (
            ["You", "!"] if multiplier > 0 else ["The dealer", "."]
        )

        # if the result is a blackjack (regular or natural)
        if isinstance(multiplier, float):
            bj_type = "natural " if abs(multiplier) == 2 else ""
            result_str += (
                ("\n" * idx)
                + MSGS["blackjack"].format(hand_no, who_won, bj_type, end_str)
                + "\n"
            )
            print(result_str)
            return "q" if prompt_continue() else ""
        player_pts = calc_points2(game_stats["player_hands"][idx])
        gtr_pts = int(max(player_pts, dealer_pts))
        lsr_pts = int(min(player_pts, dealer_pts))
        result_str += (
            ("\n" * idx)
            + MSGS["won_lost"].format(
                hand_no, who_won, gtr_pts, lsr_pts, end_str
            )
            + "\n"
        )
        print(result_str)
        return "q" if prompt_continue() else ""


def calc_winnings(results: list, game_stats: dict) -> list:
    winnings = []
    for idx, multiplier in enumerate(results):
        winnings.append(int(multiplier * game_stats["bets"][idx]))
    return winnings


def print_winnings(winnings: list, game_stats: dict) -> str:
    result_str = ""
    for idx, amount in enumerate(winnings):
        hand_no = f"Hand {idx + 1}: " if len(winnings) > 1 else ""
        if amount == 0:
            result_str += ("\n" * idx) + MSGS["push"].format(hand_no) + "\n"
            continue
        won_lost = "won" if amount > 0 else "lost"
        result_str += (
            ("\n" * idx)
            + MSGS["money_won_lost"].format(hand_no, won_lost, abs(amount))
            + "\n"
        )

        reprint_hands(game_stats, reveal=True)
        print(result_str)
        return "q" if prompt_continue() else ""

    game_stats["cash"][0] += sum(winnings)
    reprint_hands(game_stats, reveal=True)
    print(result_str)
    print(MSGS["cash_on_hand"].format(game_stats["cash"][0]))
    return "q" if prompt_continue() else ""


# MAIN FUNCTION
def twenty_one() -> None:
    clear_screen()

    # print welcome message
    print(f"{MSGS['welcome']}\n")
    if prompt_continue() == "q":
        print(f"{MSGS['goodbye']}\n")
        return
    clear_screen()

    # prompt user for mode, H17 / S17
    mode = prompt_mode()  # 1 is H17, 2 is S17
    if mode == "q":
        print(f"{MSGS['goodbye']}\n")
        return
    clear_screen()

    # prompt user for cash on hand
    cash = prompt_cash()
    if cash == "q":
        print(f"{MSGS['goodbye']}\n")
        return

    # shuffle deck, set shuffle point and round number
    deck = shuffle_deck()
    shuffle_point = random.randint(21, 41)
    round_no = [1]

    # each loop is 1 round of play
    while True:
        clear_screen()
        # reshuffle after drawing a random number of cards between 21-41
        if len(deck) < shuffle_point:
            deck = shuffle_deck()
            shuffle_point = random.randint(21, 41)
            print(f"{MSGS['deck_shuffled']}\n")
            if prompt_continue() == "q":
                break
            clear_screen()

        # prompt user for their bet
        bets = prompt_bet(cash)
        if bets == "q":
            break
        clear_screen()

        # deal cards and display them along with round number, wager, and cash
        dealer_hands, player_hands = deal_cards(deck)
        game_stats = {
            "deck": deck,
            "dealer_hands": dealer_hands,
            "player_hands": player_hands,
            "bets": bets,
            "cash": cash,
            "round_no": round_no,
        }
        reprint_hands(game_stats)

        # prompt user to split if they have a non-Ace pair
        if player_hands[0][0] == player_hands[0][1] != ACE:
            if prompt_split(player_hands, bets) == "q":
                break

        # player's turn on all of their hands, including double-down option
        if player_turn2(game_stats) == "q":
            break

        # remove all empty lists (busts, and/or unused 2nd list for split)
        # from player_hands and bets
        remove_empty_lists(player_hands)
        remove_empty_lists(bets)

        # end the loop if the player busts
        if not player_hands:
            dealer_hands[0].clear()
            # if player still has cash, play again?
            if cash[0]:
                if prompt_repeat(game_stats) in "nq":
                    break
                round_no[0] += 1
                continue
            # if player is out of cash, end program
            reprint_hands(game_stats)
            print(MSGS["out_of_cash"])
            print()
            break

        # if player hasn't bust, dealer's turn
        if dealer_turn(game_stats, mode) == "q":
            break

        # remove empty list (bust) from dealer_hands
        remove_empty_lists(dealer_hands)

        # end the loop if the dealer busts
        if not dealer_hands:
            # if player still has cash, play again?
            if cash[0]:
                if prompt_repeat(game_stats) in "nq":
                    break
                round_no[0] += 1
                continue
            # if player is out of cash, end program
            reprint_hands(game_stats)
            print(MSGS["out_of_cash"])
            print()
            break

        # reveal dealer's hole card
        reprint_hands(game_stats, reveal=True)
        reveal_hole_card(game_stats)

        if prompt_continue() == "q":
            break

        results = []
        for idx in range(len(player_hands)):
            results.append(get_winner(idx, game_stats))
            # results is a list of up to 2 ints or floats
            # these values are multiplied by the bet/s
            # at the corresponding indices to get winnings
            # winnings's sign indicates win or loss

        # print win/loss results of each of player's hands
        if print_results(results, game_stats):
            break

        # calculate how much player won or lost on each hand
        payouts = calc_winnings(results, game_stats)

        # print how much player won or lost on each hand
        if print_winnings(payouts, game_stats):
            break

        # prompt user to play again if they have cash
        if cash[0]:
            if prompt_repeat(game_stats) in "nq":
                break
            round_no[0] += 1
        # if user is out of cash, end the loop
        else:
            reprint_hands(game_stats, reveal=True)
            print(MSGS["out_of_cash"])
            print()
            break

    # thanks for playing message
    print(f"{MSGS['thanks']}\n")


twenty_one()
