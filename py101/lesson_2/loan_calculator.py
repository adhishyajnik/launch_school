import locale
import json

def localize():
    try:
        lang = locale.getlocale()[0][0:2]
    except (TypeError, ValueError):
        lang = "en"

    with open("loan_calculator_messages.json", "r") as file:
        all_langs = json.load(file)

    messages = all_langs[lang] if lang in all_langs else all_langs["en"]
    errors = messages["errors"]
    return [messages, errors]

def box_print(message):
    length = len(message)
    horiz_bord = "+-" + ("-" * length) + "-+"
    empty_line = "| " + (" " * length) + " |"

    print(f'\n{horiz_bord}\n'
          f'{empty_line}\n'
          f'| {message} |\n'
          f'{empty_line}\n'
          f'{horiz_bord}\n')

def small_box_print(message):
    length = len(message)
    horiz_bord = "+-" + ("-" * length) + "-+"

    print(f'\n{horiz_bord}\n'
          f'| {message} |\n'
          f'{horiz_bord}\n')

def get_amount():
    correct = None
    while not correct:
        small_box_print(msgs["$_prompt"])
        loan_amount = input()
        while is_loan_invalid(loan_amount):
            loan_amount = input()
        loan_disp = float(loan_amount)
        small_box_print(f"${loan_disp:.2f}{msgs['confirm']}")
        if input().casefold() in AFFIRMATIVES:
            correct = True
    return loan_amount

def get_apr():
    correct = None
    while not correct:
        small_box_print(msgs["%_prompt"])
        loan_apr = input()
        while is_percent_invalid(loan_apr):
            loan_apr = input()
        small_box_print(f"{loan_apr}%{msgs['confirm']}")
        if input().casefold() in AFFIRMATIVES:
            correct = True
    return loan_apr

def get_term():
    correct = None
    while not correct:
        small_box_print(msgs["t_prompt"])
        loan_term = input()
        while is_term_invalid(loan_term):
            loan_term = input()
        plural = msgs["sing_yr"] if float(loan_term) == 1 else msgs["plur_yr"]
        small_box_print(f"{loan_term} {plural}{msgs['confirm']}")
        if input().casefold() in AFFIRMATIVES:
            correct = True
    return loan_term

def is_loan_invalid(amount_str):
    try:
        float(amount_str)
    except (ValueError, TypeError):
        small_box_print(errs["$_invalid_1"])
        return True
    if float(amount_str) <= 0:
        small_box_print(errs["$_invalid_2"])
        return True
    if float(amount_str) * 100 != int(float(amount_str) * 100):
        small_box_print(errs["$_invalid_3"])
        return True
    return False

def is_percent_invalid(apr_str):
    try:
        float(apr_str)
    except (ValueError, TypeError):
        small_box_print(errs["%_invalid_1"])
        return True
    if float(apr_str) < 0:
        small_box_print(errs["%_invalid_2"])
        return True
    return False

def is_term_invalid(term_str):
    try:
        float(term_str)
    except (ValueError, TypeError):
        small_box_print(errs["t_invalid_1"])
        return True
    if float(term_str) <= 0:
        small_box_print(errs["t_invalid_2"])
        return True
    return False

def get_monthly_payment(principal, int_rate, duration):
    monthly_percent = (int_rate * .01) / 12
    term_months = duration * 12
    if monthly_percent > 0:
        return round(principal *\
            (monthly_percent /\
            (1 - (1 + monthly_percent) ** (-term_months))), 2)
    return round((principal / term_months), 2)

msgs, errs = localize()[0], localize()[1]

AFFIRMATIVES = msgs["yes"]

box_print(msgs["hello"])

AGAIN = True
while AGAIN:
    user_principal = float(get_amount())

    user_int_rate = float(get_apr())

    user_duration = float(get_term())

    user_monthly_payment = get_monthly_payment(
        user_principal,
        user_int_rate,
        user_duration
        )

    box_print(f"{msgs['result']} ${user_monthly_payment:.2f}")

    small_box_print(msgs["another"])
    if input().casefold() in AFFIRMATIVES:
        AGAIN = True
    else:
        box_print(msgs["goodbye"])
        AGAIN = False