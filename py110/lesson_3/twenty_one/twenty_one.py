import os
import random

"""
set mode to user input: do you want to play H17 (easy) or S17 (hard)                                                                    *
    H17: dealer stays if they have hard 17 or greater
    S17: dealer stays if they have soft 17 or greater
prompt the user for player_cash (integer)                                                                                               *
initialize deck (list of strings)
set shuffle_point to a random number between 21-41 (integer)
set repeat to True

while repeat:
    if deck has less than shuffle_point cards remaining:
        set deck to new deck
        set shuffle_point to a new random number between 21-41

    prompt user for player_bet                                                                                                          *
        player_bet stores the integer twice in a list; if user bets $5, player_bet = [5, 5]
        the second element of player_bet is used if the player splits a pair

    deal cards to dealer_hand and player_hands
        NOTE: player_hands stores the cards in the first list in a list; if user is dealt a 2 and 4, player_hands = [[2, 4], []]
        the second element of player_hands is used if the player splits a pair
        NOTE: dealer_hand only stores one hand as a single list: [card, card]

    if the user has a non-Ace pair:
        prompt user if they want to split                                                                                               *
        if user splits:
            player_hands becomes [[card], [card]]

    initialize double_down to False
    for each idx, hand in enumerate(player_hands):
        if hand is not empty:
            set double_down to user input: Do you want to double down?                                                                  *
                # return "no" responses as None
            if double_down:
                player_bet[idx] doubles
                one card is dealt to the user

                # did player bust
                player_value is the calculated value of hand
                if player_value > 21:
                    player_hands[idx] becomes "bust"
            else:
                while player_hands[idx] isn't "bust":
                    set user_action to user input: Do you want to hit or stay?                                                          *
                    if the user_action = "hit":
                        one card is dealt to the user
                        
                        # did player bust
                        player_value is the calculated value of hand
                        if player_value > 21:
                            player_hands[idx] becomes "bust"
    
    # payout bets on player busts
    for each idx, hand in enumerate(player_hands):
        if hand is "bust":
            player_bet[idx] is subtracted from player_cash
            player_hands[idx] becomes []

    # remove all empty lists (busts, and/or unused 2nd list for split) from player_hands
    [hand for hand in player_hands if hand]
        # no split and a bust becomes []
        # a split and 1 bust becomes [[card, card]]
        # a split and 2 busts becomes []
    
    # dealer's turn if the player hasn't busted
    if player_hands isn't empty:
        if mode is H17:
            dealer_value is the calculated value of dealer_hand; Aces = 1

        elif mode is S17:
            dealer_value is the calculated value of dealer_hand; Aces = 11

        while dealer_value < 17:
            one card is dealt to the dealer

            # did dealer bust
            dealer_value is the calculated value of dealer_hand; Ace value based on H17/S17
            if dealer_value > 21:
                dealer_hand becomes []

        # payout bets on dealer bust
        if dealer_hand is []:
            for each idx, hand in enumerate(player_hands):
                player_bet[idx] is added to player_cash

    # reveal dealer's cards if they haven't busted
    if dealer_hand isn't empty:
        reveal dealer cards
        dealer_value is the calculated value of dealer_hand; Ace value based on H17/S17

        # determine winner of both hands in player_hands vs dealer_hand
        for each idx, hand in enumerate(player_hands):
            player_value is the calculated value of hand

            # player gets 21
            if player_value is 21:
                if player_hand has 2 cards and dealer_hand has more than 2 cards:
                    # player got a natural blackjack
                    player_bet[idx] * 1.5 is added to player_cash
                
                elif dealer_hand has 2 cards and player_hand has more than 2 cards:
                    # dealer got a natural blackjack
                    player_bet[idx] is subtracted from player_cash
            
            # player beats dealer outright
            elif player_value is greater than dealer_value:
                player_bet[idx] is added to player_cash
            
            # dealer beats player outright
            elif dealer_value is greater than player_value:
                player_bet[idx] is subtracted from player_cash
            
            # dealer and player tie
            elif player_value and dealer_value are the same:
                push, no winner this round
    
    # display results
    # set repeat to user input: Do you want to play again?                                                                              *
        # return "yes" values as True and "no" values as False
"""


if True:  # Constants
    CONSOLE_SIZE = 79

    SUITS = 4

    FACE_CARDS = ["Jack", "Queen", "King"]

    ACE = "Ace"  # old

    CARD_RANKS = [str(num) for num in range(2, 11)] + FACE_CARDS + [ACE]  # old

    FACE_CARD_VALUE = 10  # old

    ACES = {"high": 11, "low": 1}  # old

    POINT_VALUES = (
        {str(num): num for num in range(2, 11)}
        | {card: 10 for card in FACE_CARDS}
        | {"Ace": {"High": 11, "Low": 1}}
    )

    BLACKJACK = 21

    INITIAL_DEAL = 2

    DEALER_HIT_THRESHOLD = 17

    P_CHOICES_ERR = "Invalid input"

    P_CASH_ERR = "Please enter a valid whole number."

    OUTCOMES = {
        "blackjack win": 1.0,
        "natural win": 1.5,
        "blackjack loss": -1.0,
        "natural loss": -1.0,
        "blackjack push": 0.0,
        "win": 1,
        "loss": -1,
        "push": 0,
    }

    OUTCOME_STRINGS = {
        "1.0": "You won with a blackjack!",
        "1.5": "You won with a natural blackjack!",
        "-1.0": "The dealer won with a blackjack.",
        "0.0": "Push. You both have blackjacks. No winner this round.",
        "1": "You won [player_value] to [dealer_value].",
        "-1": "You lost [player_value] to [dealer_value].",
        "0": "You tied the dealer. Push. No winner this round.",
    }

    AN_NOUNS = ["8", "Ace"]

    WELCOME_MSG = ""

    MODES_MSG = """Would you like to play (1) H17 or (2) S17?
H17: The dealer counts their aces as  1 point
     and hits until their hand is worth 17 points or more
S17: The dealer counts their aces as 11 points and
     hits until their hand is worth 17 points or more"""


"""
older functions below --------------------------------------------------------------------------------------------
"""


# keep
def clear_screen():
    _ = os.system("clear")


# keep
def shuffle_deck():
    deck = CARD_RANKS * SUITS
    random.shuffle(deck)
    return deck


# keep
def place_bet(cash):
    while True:
        user_bet = prompt_cash_value(
            f"You have ${cash} - how much would you like to wager?\n"
        )
        if user_bet == "q":
            return "q"
        if user_bet <= cash:
            return [user_bet]
        print("\nPlease place a bet that you can afford.\n")


# keep
def get_article(card):
    return "an" if card in AN_NOUNS else "a"


# delete
def print_first_card(hand):
    unknowns = len(hand) - 1
    plural = "s" if unknowns > 1 else ""
    print(f"{get_article(hand[0])} {hand[0]} and {unknowns} unknown card{plural}.")


# keep
def print_hand(hand: list, hide_hole=None) -> None:
    if hide_hole is not None:  # i.e. this is the dealer's hand
        hole_card = hand[1]
        output = "The dealer has "
        hole_str = f"and {get_article(hole_card)} {hole_card}."
        if hide_hole:
            hole_str = "and an unknown card."
        for idx, card in enumerate(hand):
            if idx != 1:
                if len(hand) > 2:
                    output += f"{get_article(card)} {card}, "
                else:
                    output += f"{get_article(card)} {card} "
        output += hole_str
    else:  # i.e. this is the player's hand, or one of them
        output = "You have "
        for card in hand[:-1]:
            if len(hand) > 2:
                output += f"{get_article(card)} {card}, "
            else:
                output += f"{get_article(card)} {card} "
        output += f"and {get_article(hand[-1])} {hand[-1]}."

    print(output)


# keep
def print_hands(dealer_hand, player_hands, hide_hole=True):
    print_hand(dealer_hand, hide_hole)
    if isinstance(
        player_hands[0], list
    ):  # if the function is passed player_hands: [["card", "card"], ["card", "card"]]
        for idx, hand in enumerate(player_hands):
            if len(player_hands) > 1:
                # prefix with hand number if player has 2 active hands
                print(f"Hand {idx + 1}:", end=" ")
            print_hand(hand)
    else:  # if the function is passed player_hands[0] or player_hands[1]: ["card", "card"]
        print_hand(player_hands)


def print_wager(bet, cash):
    print(f"WAGER: ${bet}        CASH IN HAND: ${cash}")


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


"""
older functions above --------------------------------------------------------------------------------------------
"""


def prompt_continue() -> None | str:
    print("Press Enter to continue or 'q' to quit.")
    if input().casefold() == "q":
        return "q"


# for setting mode (H17 / S17) and user action (hit / stay)
def prompt_choices(message: str, choices: dict, error_message=P_CHOICES_ERR) -> str:
    print(message)
    while True:
        user_input = input().strip().casefold()
        if user_input == "q" or user_input in choices.values():
            return user_input
        if user_input in choices:
            return choices[user_input]
        print(error_message)


# for splitting, doubling down, and playing again
def prompt_yes_or_no(message: str) -> str:
    message += " (y) Yes or (n) No:"
    return prompt_choices(
        message, {"y": "yes", "n": "no"}, "Please enter y, n, yes, or no"
    )


# for getting player cash and player bets
def prompt_cash_value(message: str, error_message=P_CASH_ERR) -> int | str:
    print(message)
    while True:
        user_input = input("$").strip()
        if user_input == "q":
            return "q"
        try:
            return int(user_input)
        except ValueError:
            print(error_message)


def deal_cards(deck: list) -> list:
    player_hands = [[]]
    dealer_hand = []
    for _ in range(INITIAL_DEAL):
        player_hands[0].append(deck.pop())
        dealer_hand.append(deck.pop())
    return [player_hands, dealer_hand]


def hit(deck: list, hand: list) -> None:
    hand.append(deck.pop())


def calculate_points(hand: list) -> int:
    total = 0
    for card in hand:
        if card != "Ace":
            total += POINT_VALUES[card]

    for card in hand:
        if card == "Ace":
            if total + POINT_VALUES["Ace"]["High"] <= BLACKJACK:
                total += POINT_VALUES["Ace"]["High"]
            else:
                total += POINT_VALUES["Ace"]["Low"]

    return total


def player_turn(deck: list, p_hands: list, d_hand: list, bets: list) -> int | str:
    payout = 0
    for idx, hand in enumerate(p_hands):
        if hand:
            if len(hand) < 2:
                hit(deck, hand)
            print_hands(d_hand, hand)

            double_down = prompt_yes_or_no("Would you like to double down?")
            if double_down == "q":
                return "q"

            if double_down == "y":
                bets[idx] *= 2
                hit(deck, hand)
                print(f"Your wager has doubled to ${bets[idx]}.")
                print(f"You drew {get_article(hand[-1])} {hand[-1]}.")

                hand_value = calculate_points(hand)
                if hand_value > BLACKJACK:
                    print("You went bust.")
                    print(f"You lost ${bets[idx]}.")
                    payout -= bets[idx]
                    hand.clear()
                    bets[idx] = None

                print("Press Enter to continue or 'q' to quit.")
                if input().casefold() == "q":
                    return "q"
            else:
                while hand:
                    user_action = prompt_choices(
                        "Do you want to (1) hit or (2) stay?",
                        {"1": "hit", "2": "stay"},
                        "Please enter 1, 2, hit, or stay",
                    )
                    if user_action == "q":
                        return "q"

                    elif user_action == "hit":
                        hit(deck, hand)
                        print(f"You drew {get_article(hand[-1])} {hand[-1]}.")

                        hand_value = calculate_points(hand)
                        if hand_value > BLACKJACK:
                            print("You went bust.")
                            print(f"You lost ${bets[idx]}.")
                            payout -= bets[idx]
                            hand.clear()
                            bets[idx] = None

                    elif user_action == "stay":
                        hand_value = calculate_points(hand)
                        print(f"You stayed at {hand_value}.")

                        print("Press Enter to continue or 'q' to quit.")
                        if input().casefold() == "q":
                            return "q"

                        break
    return payout


def dealer_turn(deck: list, hand: list, mode: str, bets: list) -> None | int | str:
    payout = 0
    print_hand(hand, hide_hole=True)
    if prompt_continue() == "q":
        return "q"
    hand_value: int = calculate_points(hand)  # Aces are high unless hand busts
    hit_below = DEALER_HIT_THRESHOLD
    if mode == "h17" and "Ace" in hand:  # hit on soft 17
        hit_below = DEALER_HIT_THRESHOLD + 1
    while hand_value < hit_below:
        hit(deck, hand)
        hand_value = calculate_points(hand)
        if hand_value > BLACKJACK:
            print("The dealer hits and busts.")
            hand.clear()
            for idx, bet in enumerate(bets):
                if len(bets) > 1:
                    print(f"On bet {idx + 1}, you won ${bet}.")
                else:
                    print(f"You won ${bet}.")
                payout += bet
            return payout
        else:
            print("The dealer hits.")
        if prompt_continue() == "q":
            return "q"
    print("The dealer stays.")


def payout_busts(bust_hands: list, bets: list) -> None | str:
    payout = 0
    hand_bet_str, won_lost, sign = "", "", 1
    if len(bust_hands) == 0:  # dealer went bust
        hand_bet_str = "bet"
        won_lost = "won"
        sign = 1
    elif list() in bust_hands:
        hand_bet_str = "hand"
        won_lost = "lost"
        sign = -1
    for idx, bet in enumerate(bets):
        if len(bust_hands) == 0:
            if len(bets) > 1:
                print(f"On {hand_bet_str} {idx + 1}, you {won_lost} ${bet}.")
            else:
                print(f"You {won_lost} ${bet}.")
            payout += bet * sign
            bets[idx] = None
        else:
            if bust_hands[idx] == []:
                if len(bets) > 1:
                    print(f"On {hand_bet_str} {idx + 1}, you {won_lost} ${bet}.")
                else:
                    print(f"You {won_lost} ${bet}.")
                payout += bet * sign
                bets[idx] = None

        if prompt_continue() == "q":
            return "q"
    return payout


def get_winner(player_hands: list, dealer_hand: list) -> list:
    dealer_value = calculate_points(dealer_hand)

    results = []
    for hand in player_hands:
        player_value = calculate_points(hand)

        # player has more points than dealer
        if player_value > dealer_value:
            # player has 21
            if player_value == BLACKJACK:
                # player has a natural (2-card) blackjack
                if len(hand) == 2:
                    results.append(OUTCOMES["natural win"])

                # player has a normal (> 2-card) blackjack
                else:
                    results.append(OUTCOMES["blackjack win"])

            # player has less than 21
            else:
                results.append(OUTCOMES["win"])

        # player has fewer points than dealer
        elif player_value < dealer_value:
            # dealer has 21
            if dealer_value == BLACKJACK:
                # dealer has a natural (2-card) blackjack
                if len(dealer_hand) == 2:
                    results.append(OUTCOMES["natural loss"])

                # dealer has a normal (> 2-card) blackjack
                else:
                    results.append(OUTCOMES["blackjack loss"])

            # dealer has less than 21
            else:
                results.append(OUTCOMES["loss"])

        # player and dealer points are tied
        else:
            # both tied with less than 21
            if player_value != 21:
                results.append(OUTCOMES["push"])

            # player has natural blackjack and dealer doesn't
            elif len(hand) == 2 != len(dealer_hand):
                results.append(OUTCOMES["natural win"])

            # dealer has natural blackjack and player doesn't
            elif len(dealer_hand) == 2 != len(hand):
                results.append(OUTCOMES["loss"])

            # player and dealer both have natural blackjacks
            # or neither have natural blackjacks
            else:
                results.append(OUTCOMES["blackjack push"])

    return results


def twenty_one() -> None:
    clear_screen()
    print(WELCOME_MSG)

    if prompt_continue() == "q":
        print("Goodbye!")
        return

    clear_screen()
    # prompt user to play H17 or S17 mode
    mode = prompt_choices(
        MODES_MSG, {"1": "h17", "2": "s17"}, "Please enter 1, 2, H17, or S17"
    )
    if mode == "q":
        print("Goodbye!")
        return
    print(f"Mode: {mode.capitalize()}")

    if prompt_continue() == "q":
        print("Goodbye!")
        return

    clear_screen()
    # prompt user for cash on hand
    player_cash = prompt_cash_value("How much money are you playing with today?")
    if player_cash == "q":
        print("Goodbye!")
        return
    print(f"Cash on hand: ${player_cash}")

    if prompt_continue() == "q":
        print("Goodbye!")
        return

    initial_cash = player_cash
    deck = shuffle_deck()
    shuffle_point = random.randint(21, 41)

    # each loop is a single round
    # repeat until player runs out of cash (quit breaks out of loop)
    round = 1
    while player_cash > 0:
        clear_screen()
        if len(deck) < shuffle_point:
            deck = shuffle_deck()
            shuffle_point = random.randint(21, 41)
            print("The deck has been shuffled.")

        player_bets = place_bet(player_cash)
        if player_bets == "q":
            break
        print(f"Your wager: ${player_bets[0]}")

        # continue
        if prompt_continue() == "q":
            break

        player_hands, dealer_hand = deal_cards(deck)

        clear_screen()
        print_hands(dealer_hand, player_hands[0], hide_hole=True)

        # prompt user to split if they have a non-Ace pair
        # which creates a 2nd list in player_hands and moves one card there
        if len(set(player_hands[0])) == 1 and "Ace" not in player_hands[0]:
            split = prompt_yes_or_no("Would you like to split your pair?")
            if split == "q":
                break
            if split == "y":
                player_hands.append([player_hands[0].pop()])
                player_bets *= 2
                print(f"You've split your {player_hands[0][0]}s into two hands.")

                if prompt_continue() == "q":
                    break

        clear_screen()
        # user plays their hand/s
        if player_turn(deck, player_hands, dealer_hand, player_bets) == "q":
            break

        # payout bets on player bust/s
        # player_cash += payout_busts(player_hands, player_bets)
        """
        for idx, hand in enumerate(player_hands):
            if not hand:
                if len(player_hands) > 1:
                    print(f"On hand {idx + 1}, you lost {player_bets[idx]}.")
                else:
                    print(f"You lost {player_bets[idx]}.")
                player_cash -= player_bets[idx]
                player_bets[idx] = None
                if prompt_continue() == "q":
                    break
        """

        # remove bust hands and bets from player_hands and player_bets
        player_hands = [hand for hand in player_hands if hand]
        player_bets = [bet for bet in player_bets if bet]

        # dealer's turn if the player hasn't busted
        if player_hands:
            clear_screen()
            dealer_turn(deck, dealer_hand, mode)
            # payout bets on dealer bust
            # player_cash += payout_busts(dealer_hand, player_bets)
            """
            for idx, hand in enumerate(player_hands):
                if not dealer_hand:
                    if len(player_hands) > 1:
                        print(f"On hand {idx + 1}, you won {player_bets[idx]}.")
                    else:
                        print(f"You won {player_bets[idx]}.")
                    player_cash += player_bets[idx]
                    player_bets[idx] = None
                    if prompt_continue() == "q":
                        break
            """

        # reveal cards and display outcome if no one's busted
        if player_hands and dealer_hand:
            clear_screen()
            print_hands(dealer_hand, player_hands, hide_hole=False)
            # results is a list of bet multipliers for each of player's hands
            results = get_winner(player_hands, dealer_hand)
            dealer_value = calculate_points(dealer_hand)
            # print outcome of each of player's hands
            for idx, bet_multiplier in enumerate(results):
                hand_value = calculate_points(player_hands[idx])
                winnings = int(bet_multiplier * player_bets[idx])
                won_lost = "won" if winnings > 0 else "lost"
                outcome_str = (
                    OUTCOME_STRINGS[str(bet_multiplier)]
                    .replace("[player_value]", str(hand_value))
                    .replace("[dealer_value]", str(dealer_value))
                )
                # prefix result with hand number if there's more than 1 hand
                if len(results) > 1:
                    outcome_str = outcome_str.casefold()
                    print(f"On hand {idx + 1},", end=" ")
                print(outcome_str)
                # print winnings and add to player_cash
                print(f"You {won_lost} ${abs(winnings)}.")
                player_cash += winnings

        if player_cash > 0:
            # display user's updated cash on hand
            print(f"You now have ${player_cash} on hand.")

            if prompt_continue() == "q":
                break

            # play again
            if prompt_yes_or_no("Do you want to play another hand?") in ["n", "q"]:
                net = player_cash - initial_cash
                if net > 0:
                    print(
                        f"You won ${net} and walked away with a total of ${player_cash}."
                    )
                elif net < 0:
                    print(
                        f"You lost ${-net} and walked away with a total of ${player_cash}."
                    )
                else:
                    print(
                        f"You walked away with the same amount you started with: ${player_cash}."
                    )
                break
        else:
            print("You're out of cash!")
            break

        round += 1

    print("Thanks for playing!")


# twenty_one()

# payout_busts([[]], [10])  # lost 10
# payout_busts([], [10])  # won 10
# payout_busts([[], []], [10, 5])  # hand 1: lost 10, hand 2: lost 5
# payout_busts([], [10, 5])  # bet 1: won 10, bet 2: won 5
# payout_busts([[], ["2", "4"]], [10, 5])  # hand 1: lost 10
# payout_busts([["2", "4"], []], [10, 5])  # hand 2: lost 5
# payout_busts([["2", "4"]], [5])  # 0
# payout_busts([["2", "4"]], [10, 5])  # 0
# payout_busts([["2", "4"], ["6", "8"]], [10, 5])  # 0
