print('Welcome to Calculator!\n'
      'Enter the first number.')
number1 = int(input())

print('Enter the second number.')
number2 = int(input())

print('What operation would you like to perform?\n'
      '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

match operation:
    case '1':       # 1 represents addition
        output = number1 + number2
    case '2':       # 2 represents subtraction
        output = number1 - number2
    case '3':       # 3 represents multiplication
        output = number1 * number2
    case '4':       # 4 represents division
        output = number1 / number2

print(f'The result is {output}')