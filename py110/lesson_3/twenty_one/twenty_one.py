import os
import random

"""
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.
"""

BLACKJACK = 21

DEALER_HIT_THRESHOLD = 17

CONSOLE_SIZE = 79

SUITS = 4

FACE_CARDS = ["Jack", "Queen", "King"]

ACE = "Ace"

CARD_VALUES = [str(num) for num in range(2, 11)] + FACE_CARDS + [ACE]

INITIAL_DEAL = 2

AN_NOUNS = ["8", "Ace"]

FACE_CARD_VALUE = 10

ACES = {"high": 11, "low": 1}


def clear_screen():
    _ = os.system("clear")


def prompt_user(message, valid_inputs, error_message="Invalid input\n"):
    print(message)
    while True:
        user_input = input().strip().casefold()
        if user_input == "q":
            return "q"
        if user_input in valid_inputs:
            return user_input
        print(error_message)


def prompt_dollar_amount(message, error_message="Please enter a valid whole number.\n"):
    print(message)
    while True:
        input_figure = input("$")

        if input_figure.casefold() == "q":
            return "q"

        try:
            cash = int(input_figure)
            break
        except ValueError:
            print(error_message)

    return cash


def get_cash():
    user_cash = prompt_dollar_amount("How much money are you playing with today?\n")
    if user_cash == "q":
        return "q"
    return user_cash


def shuffle_deck():
    deck = CARD_VALUES * SUITS
    random.shuffle(deck)
    return deck


def place_bet(cash):
    while True:
        user_bet = prompt_dollar_amount(
            f"You have ${cash} - how much would you like to wager?\n"
        )
        if user_bet == "q":
            return "q"
        if user_bet <= cash:
            return user_bet
        print("\nPlease place a bet that you can afford.\n")


def get_article(card):
    return "an" if card in AN_NOUNS else "a"


def deal_cards(deck):
    dealer_hand = []
    player_hand = []
    for _ in range(INITIAL_DEAL):
        dealer_hand.append(deck.pop(0))
        player_hand.append(deck.pop(0))

    return [dealer_hand, player_hand]


def print_first_card(hand):
    unknowns = len(hand) - 1
    plural = "s" if unknowns > 1 else ""
    print(f"{get_article(hand[0])} {hand[0]} and {unknowns} unknown card{plural}.")


def print_all_cards(hand):
    output = ""
    for card in hand[:-1]:
        if len(hand) > 2:
            output += f"{get_article(card)} {card}, "
        else:
            output += f"{get_article(card)} {card} "
    output += f"and {get_article(hand[-1])} {hand[-1]}."

    print(output)


def print_hands(d_hand, p_hand, reveal=False):
    print("\nThe dealer has ", end="")
    if reveal:
        print_all_cards(d_hand)
    else:
        print_first_card(d_hand)

    print("You have ", end="")
    print_all_cards(p_hand)


def print_wager(bet, cash):
    print(f"WAGER: ${bet}        CASH IN HAND: ${cash}")


def hit(deck, hand):
    hand.append(deck.pop(0))
    return hand


def calculate_points(hand):
    total = 0
    for card in hand:
        if card != "Ace":
            try:
                total += int(card)
            except ValueError:
                total += FACE_CARD_VALUE

    for card in hand:
        if card == "Ace":
            if total + ACES["high"] <= BLACKJACK:
                total += ACES["high"]
            else:
                total += ACES["low"]

    return total


def player_turn(deck, hand):
    while True:
        user_action = prompt_user(
            "\nWould you like to hit (1) or stay (2)?\n",
            ["1", "2", "hit", "stay"],
            "\nPlease enter '1' to hit, '2' to stay, or 'hit' or 'stay'.\n",
        )

        match user_action.casefold():
            case "q":
                print("")
                return "q"
            case a if a in ["2", "stay"]:
                points = calculate_points(hand)
                print(f"\nYou stayed at {points}.\n")
                return hand
            case b if b in ["1", "hit"]:
                hand = hit(deck, hand)
                article = get_article(hand[-1])
                print(f"\nYou drew {article} {hand[-1]}")

        points = calculate_points(hand)
        if points > BLACKJACK:
            print("\nYou went bust. The dealer wins.\n")
            if input("Press Enter to continue.\n").casefold() == "q":
                print("")
                return "q"
            return "bust"


def dealer_turn(deck, hand):
    while calculate_points(hand) < DEALER_HIT_THRESHOLD:
        hand = hit(deck, hand)
        print("\nThe dealer hits.\n")

        if input("Press Enter to continue.").casefold() == "q":
            print("")
            return "q"

        if calculate_points(hand) > BLACKJACK:
            print("The dealer went bust. You win.\n")
            if input("Press Enter to continue.").casefold() == "q":
                print("")
                return "q"
            return "bust"

    print("\nThe dealer stays.\n")
    return hand


def get_winner(d_hand, p_hand):
    results = {
        "you": {"points": calculate_points(p_hand), "cards": len(p_hand)},
        "the dealer": {"points": calculate_points(d_hand), "cards": len(d_hand)},
    }

    if results["you"]["points"] > results["the dealer"]["points"]:
        return [
            list(results.keys())[0],
            results["you"]["points"],
            results["the dealer"]["points"],
        ]
    elif results["you"]["points"] < results["the dealer"]["points"]:
        return [
            list(results.keys())[1],
            results["the dealer"]["points"],
            results["you"]["points"],
        ]
    elif results["you"]["points"] == results["the dealer"]["points"] < BLACKJACK:
        return ["push", results["the dealer"]["points"], results["you"]["points"]]
    elif results["you"]["points"] == results["the dealer"]["points"] == BLACKJACK:
        hand_sizes = [results["you"]["cards"], results["the dealer"]["cards"]]
        if hand_sizes.count(2) == 1:
            win_idx = hand_sizes.index(2)
            return [list(results.keys())[win_idx], "got a blackjack!"]
        else:
            return ["push", results["the dealer"]["points"], results["you"]["points"]]


def print_winner(results):
    if results[0] in ["you", "the dealer"] and len(results) == 3:
        print(f"\n{results[0].capitalize()} won {results[1]} to {results[2]}.\n")
    elif results[0] == "push":
        print("\nPush. No winner this round.\n")
    else:
        print(f"\n{results[0].capitalize()} won -- {results[0]} {results[1]}\n")


def payout_bets(results, bet, cash):
    if results[0] in ["you", "The dealer busts."]:
        cash += bet
    elif results[0] in ["the dealer", "You bust."]:
        cash -= bet

    return cash


def is_game_over(cash):
    return True if cash <= 0 else False


def twenty_one():
    round = -1
    new_deck = shuffle_deck()

    clear_screen()

    while True:
        if round >= 0:
            if (
                input("Press Enter to play again or enter 'q' to quit.").casefold()
                == "q"
            ):
                break

        clear_screen()

        round += 1
        if round == 0:
            player_cash = get_cash()
            if player_cash == "q":
                print("")
                break

        if len(new_deck) < 24:
            new_deck = shuffle_deck()
            print("\nThe deck has been shuffled.\n")
            if input("Press Enter to continue.\n").casefold() == "q":
                print("")
                break

        clear_screen()
        player_bet = place_bet(player_cash)
        if player_bet == "q":
            print("")
            break

        dealer_hand, player_hand = deal_cards(new_deck)

        clear_screen()
        print_wager(player_bet, player_cash)
        print_hands(dealer_hand, player_hand)

        player_hand = player_turn(new_deck, player_hand)
        if player_hand == "q":
            break
        if player_hand == "bust":
            player_cash = payout_bets(["You bust."], player_bet, player_cash)
            if is_game_over(player_cash):
                print("You're out of cash!\n")
                break
            else:
                print(f"You have ${player_cash}.\n")
                if input("Press Enter to continue.\n").casefold() == "q":
                    break
                continue

        clear_screen()
        print_wager(player_bet, player_cash)
        print_hands(dealer_hand, player_hand)

        dealer_hand = dealer_turn(new_deck, dealer_hand)
        if dealer_hand == "q":
            break
        if dealer_hand == "bust":
            player_cash = payout_bets(["The dealer busts."], player_bet, player_cash)
            if is_game_over(player_cash):
                print("You're out of cash!\n")
                break
            else:
                print(f"You have ${player_cash}.\n")
                if input("Press Enter to continue.\n").casefold() == "q":
                    break
                continue

        if input("Press Enter to reveal.\n").casefold() == "q":
            break

        clear_screen()
        print_wager(player_bet, player_cash)
        print_hands(dealer_hand, player_hand, True)

        results = get_winner(dealer_hand, player_hand)

        print_winner(results)
        if input("Press Enter to continue.\n").casefold() == "q":
            break

        player_cash = payout_bets(results, player_bet, player_cash)
        if is_game_over(player_cash):
            print("You're out of cash!\n")
            break
        else:
            print(f"You have ${player_cash}.\n")
            if input("Press Enter to continue.\n").casefold() == "q":
                break

    print("Thanks for playing!\n")


twenty_one()
