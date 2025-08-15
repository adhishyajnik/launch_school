# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 6: Flow Control

def even_or_odd(number):
    print(f'{number} is even' if number % 2 == 0 else f'{number} is odd')

user_num = int(input('Enter an integer: '))

even_or_odd(user_num)