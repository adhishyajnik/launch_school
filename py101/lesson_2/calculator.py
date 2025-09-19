import locale
import json

try:
    LANG = locale.getlocale()[0][0:2]
except TypeError:
    LANG = 'en'

# load all message strings from json file to all_langs dictionary
with open('calculator_messages.json', 'r') as file:
    all_langs = json.load(file)

# extract the correct translations and assign to msgs dictionary
msgs = {}
if LANG in all_langs:
    msgs = all_langs[LANG]
else:
    msgs = all_langs['en']

def prompt(prompt_message):
    print(f'==> {prompt_message}')

def get_number(nth):
    num_prompt = 'prompt' + str(nth)
    prompt(msgs[num_prompt])
    num = input()
    while invalid_number(num):
        prompt(msgs['num_err'])
        num = input()
    return num

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_ops_line2(number_str):
    if float(number_str) == 0:
        return msgs['3op_string']
    return msgs['4op_string']

def get_ops_list(number_str):
    if float(number_str) == 0:
        return msgs['3op_list']
    return msgs['4op_list']

def get_ops_error(number_str):
    if float(number_str) == 0:
        return msgs['3op_err']
    return msgs['4op_err']

def get_operation(operand2):
    second_line = get_ops_line2(operand2)
    valid_ops_list = get_ops_list(operand2)
    repeat_str = get_ops_error(operand2)

    prompt(f"{msgs['prompt3']}{second_line}")
    op_choice = input()
    while op_choice not in valid_ops_list:
        prompt(repeat_str)
        op_choice = input()
    return op_choice

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

    number1 = get_number(1)

    number2 = get_number(2)

    operation = get_operation(number2)

    calc_result = find_result(number1, number2, operation)

    prompt(f"{msgs['result']} {calc_result}")

    prompt(msgs['another'])
    AGAIN = input().casefold() in (msgs['yes'], msgs['yes'][0])