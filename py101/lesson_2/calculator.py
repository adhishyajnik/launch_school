def prompt(prompt_message):
    print(f'==> {prompt_message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

AGAIN = True
while AGAIN:

    prompt("What's the first number?")
    number1 = input()
    while invalid_number(number1):
        prompt('Please enter a valid integer.')
        number1 = input()

    prompt("What's the second number?")
    number2 = input()
    while invalid_number(number2):
        prompt('Please enter a valid integer.')
        number2 = input()

    prompt('What operation would you like to perform?\n'
        '1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()
    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':
            result = int(number1) + int(number2)
        case '2':
            result = int(number1) - int(number2)
        case '3':
            result = int(number1) * int(number2)
        case '4':
            result = int(number1) / int(number2)

    prompt(f'The result is {result}')

    prompt('Would you like to perform another calculation? (yes/no)')
    AGAIN = bool(input() == 'yes')