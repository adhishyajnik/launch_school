from launch_school.py110.lesson_3.twenty_one.twenty_one import (
    BLACKJACK,
    DEALER_HIT_THRESHOLD,
    calculate_points,
    hit,
)


def dealer_turn(deck: list, hand: list, mode: str) -> None:
    hand_value = calculate_points(hand)  # Aces are high unless hand busts
    # hit on soft 17
    if mode == "h17" and "Ace" in hand:
        while hand_value <= DEALER_HIT_THRESHOLD:
            hit(deck, hand)
            hand_value = calculate_points(hand)
            if hand_value > BLACKJACK:
                hand.clear()
    if mode == "s17":
        while hand_value < DEALER_HIT_THRESHOLD:
            hit(deck, hand)
            hand_value = calculate_points(hand)
            if hand_value > BLACKJACK:
                hand.clear()
