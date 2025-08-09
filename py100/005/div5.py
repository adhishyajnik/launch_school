# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 5: Functions and Methods

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

check_1 = all(remainders_5(numbers_1))
if check_1 == True:
    print('numbers_1 doesn\'t have any numbers divisible by 5')

check_2 = all(remainders_5(numbers_2))
if check_2 == True:
    print('numbers_2 doesn\'t have any numbers divisible by 5')

check_3 = all(remainders_5(numbers_3))
if check_3 == True:
    print('numbers_3 doesn\'t have any numbers divisible by 5')

check_4 = all(remainders_5(numbers_4))
if check_4 == True:
    print('numbers_4 doesn\'t have any numbers divisible by 5')