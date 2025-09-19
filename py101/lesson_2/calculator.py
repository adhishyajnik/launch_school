import locale
import json

lang = locale.getlocale()[0][0:2]

# load all message strings from json file to all_langs dictionary
with open('calculator_messages.json', 'r') as file:
    all_langs = json.load(file)

# extract the correct translations and assign to msgs dictionary
msgs = {}
if lang in all_langs:
    msgs = all_langs[lang]
else:
    msgs = all_langs['en']

def prompt(prompt_message):
    print(f'==> {prompt_message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_valid_ops(number_str):
    if float(number_str) == 0:
        return [
            msgs['3op_string'],
            msgs['3op_list'],
            msgs['3op_err'],
            ]
    return [
        msgs['4op_string'],
        msgs['4op_list'],
        msgs['4op_err'],
        ]

def find_result(num1, num2, op):
    match op:
        case '1':
            result = float(num1) + float(num2)
        case '2':
            result = float(num1) - float(num2)
        case '3':
            result = float(num1) * float(num2)
        case '4':
            result = float(num1) / float(num2)
    return int(result) if result == int(result) else result

prompt(msgs['welcome'])

AGAIN = True
while AGAIN:

    prompt(msgs['prompt1'])
    number1 = input()
    while invalid_number(number1):
        prompt(msgs['num_err'])
        number1 = input()

    prompt(msgs['prompt2'])
    number2 = input()
    while invalid_number(number2):
        prompt(msgs['num_err'])
        number2 = input()

    second_line = get_valid_ops(number2)[0]
    valid_ops_list = get_valid_ops(number2)[1]
    repeat_str = get_valid_ops(number2)[2]

    prompt(f"{msgs['prompt3']}{second_line}")
    operation = input()
    while operation not in valid_ops_list:
        prompt(repeat_str)
        operation = input()

    calc_result = find_result(number1, number2, operation)

    prompt(f"{msgs['result']} {calc_result}")

    prompt(msgs['another'])
    AGAIN = bool(input() == msgs['yes'])