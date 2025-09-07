import os
from random import randint as r

def d6():
    # Commented code loops through random numbers before landing on one
    for i in range(1, 25000):
        res = r(1, 6)
        print(f' Rolling: {res}', end='\r')
    print('', end='\r')
    res = r(1, 6)
    return res

def get_event_index(roll_result):
    cat = None
    if roll_result % 2 == 0:
        cat = roll_result / 2
        return int(cat - 1)
    else:
        cat = ((roll_result + 1) / 2)
        return int(cat - 1)

def result_pts_str(points):
    output_str = ""
    for num in points:
        suffixes = ["Scandal", "Masterpiece", "Stress"]
        cur_index = points.index(num)
        if num < 0:
            output_str = output_str + str(points[cur_index]) + " " + suffixes[cur_index] + "  "
        elif num > 0:
            output_str = output_str + "+" + str(points[cur_index]) + " " + suffixes[cur_index] + "  "
    return output_str

SCORE_CATEGORIES = ['Scandal', 'Masterpiece', 'Stress']

scores = [0, 0, 0]
six_counter = 0
prev_rolls = []

def update_scores(points):
    global scores
    for i in range(3):
        scores[i] += points[i]
    return scores

def reduce_to_zero(score_category):
    global scores
    scores[score_category] = 0
    return scores

INTRO = '''
Trapped in a Cabin With Lord Byron
A game based on Oliver Darkshire's 1-page RPG

You are on vacation with Lord Byron in his holiday home,
but the weather has trapped you and your friends inside.
Only the strong will survive.'''

EVENTS = ("Byron's Recreations", "Byron's Drama", "A Brief Redoubt...")

OUTCOMES = {
    "Byron's Recreations": (
        ("Is he aware the walls are exceptionally thin?", [0, 0, 1]),
        ("He's made a mess of your desk in the process", [0, -1, 0]),
        ("May he borrow your husband? Of course.", [1, 0, -1]),
        ("His half-sister is here, and they are far too intimate", [2, 0, 0]),
        ("You are weary of listening to tales of his exploits", [0, 0, 1]),
        ("He makes an excellent muse on occasion", [0, 2, -1]),
    ),
    "Byron's Drama": (
        ("He needs help reading his fan mail", [0, 0, 1]),
        ("He's brought his pet bear. It is not trained.", [0, 0, 2]),
        ("He wants you to read his poetry", [0, 0, 3]),
        ("He's in the papers. Again. Which means you are too.", [1, 0, 0]),
        ("He broke up with his latest girlfriend/boyfriend", [2, 0, 0]),
        ("He's found a new skull to use as a goblet", [3, 0, 0]),
    ),
    "A Brief Redoubt...": (
        ("Time alone. Blissful time.", [0, 1, 0]),
        ("He's busy with a paramour.", [0, 0, -1]),
        ("A walk around the house! Underwear on our heads!", [1, 0, 0]),
        ("He has an excellent supply of contraband substances.", [1, 1, 0]),
        ("Wine! A chest of wine!", [0, -1, 0]),
        ("He passed out in his study", [0, 1, 0]),
    ),
}

OUTROS = [
'''You are no longer fit to enter society
and must flee to nurse your reputation.''',
'''You create a new genre of supernatural horror fiction
based on your time with Byron.''',
'''You lose your patience with the man and either
kill him in a fit of rage or otherwise descend into
uncontrollable weeping from which you never emerge.''',
]

def turn():
    global six_counter
    global prev_rolls

    six_counter = 0

    roll1 = d6()
    roll2 = d6()

    prev_rolls.append(roll1)
    prev_rolls.append(roll2)

    prev_rolls_str = ''
    for num in prev_rolls:
        prev_rolls_str += str(num)
    
    if len(prev_rolls) > 2:
        prev_rolls.pop(0)
        prev_rolls.pop(0)

    if '666' not in prev_rolls_str:
        cur_evt = EVENTS[get_event_index(roll1)]
        outcome = OUTCOMES[cur_evt][roll2 - 1]
        cur_msg = outcome[0]
        raw_pts = outcome[1]
        
        pts_won = result_pts_str(raw_pts)
        update_scores(raw_pts)
    else:
        six_counter = prev_rolls.count(6)
        cur_evt = f'You rolled {six_counter} sixes in a row.'
        cur_msg = '''Byron destroys your manuscript either by accident
        or on purpose suring one of his episodes.'''

        evt_ind = r(0, 2)
        cat_scr = SCORE_CATEGORIES[evt_ind]
        pts_won = f'Your {cat_scr} score is reduced to 0.'
        reduce_to_zero(evt_ind)

        prev_rolls.clear()

    os.system('clear')
    print(f'\nYou rolled a {roll1} and a {roll2}.')
    print(f'\n{cur_evt}: {cur_msg} | {pts_won}')
    print(f'\nCurrent Scores:\n  Scandal: {scores[0]}\n  Masterpiece: {scores[1]}\n  Stress: {scores[2]}')

def trapped_with_byron():
    print(INTRO)

    first_turn = input('\nPress Enter to roll. Enter any text to quit.\n')
    if first_turn != '':
        return

    while True:
        turn()

        end_yet = [ score for score in scores if score >= 10 ]
        if end_yet:
            out_msg = OUTROS[scores.index(end_yet[0])]
            print(f'\n{out_msg}\n')
            return
        
        new_turn = input('\nPress Enter to roll another turn. Input any text to quit.\n')
        if new_turn != '':
            return

os.system('clear')
trapped_with_byron()