def prompt(prompt_message):
    print(f'==> {prompt_message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def get_valid_ops(number_str):
    if int(number_str) == 0:
        return [
            '1) Add 2) Subtract 3) Multiply',
            ["1", "2", "3"],
            'You must choose 1, 2, or 3',
            ]
    else:
        return [
            '1) Add 2) Subtract 3) Multiply 4) Divide',
            ["1", "2", "3", "4"],
            'You must choose 1, 2, 3, or 4',
            ]

prompt('Welcome to Calculator!')

again = True
while again == True:

    prompt('Enter the first number.')
    number1 = input()
    while invalid_number(number1) == True:
        prompt('Please enter a valid integer.')
        number1 = input()

    prompt('Enter the second number.')
    number2 = input()
    while invalid_number(number2) == True:
        prompt('Please enter a valid integer.')
        number2 = input()

    second_line = get_valid_ops(number2)[0]
    valid_ops_list = get_valid_ops(number2)[1]
    repeat_str = get_valid_ops(number2)[2]

    prompt(f'What operation would you like to perform?\n'
        f'{second_line}')
    operation = input()
    while operation not in valid_ops_list:
        prompt(repeat_str)
        operation = input()

    match operation:
        case '1':         # 1 represents addition
            result = int(number1) + int(number2)
        case '2':         # 2 represents subtraction
            result = int(number1) - int(number2)
        case '3':         # 3 represents multiplication
            result = int(number1) * int(number2)
        case '4':         # 4 represents division
            result = int(number1) / int(number2)

    if result == int(result):
        result = int(result)

    prompt(f'The result is {result}')

    prompt('Would you like to perform another calculation? (yes/no)')
    if input().lower() == 'yes':
        again = True
    else:
        again = False