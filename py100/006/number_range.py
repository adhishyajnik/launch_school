# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 6: Flow Control

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <=50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')

user_num = int(input('Enter an integer: '))
number_range(user_num)