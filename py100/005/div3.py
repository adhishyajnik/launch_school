# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 5: Functions and Methods

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

check_1 = any(remainders_3(numbers_1))
check_2 = any(remainders_3(numbers_2))
check_3 = any(remainders_3(numbers_3))
check_4 = any(remainders_3(numbers_4))

if check_1 == True:
    print('numbers_1 has a number that\'s not divisible by 3')

if check_2 == True:
    print('numbers_2 has a number that\'s not divisible by 3')

if check_3 == True:
    print('numbers_3 has a number that\'s not divisible by 3')

if check_4 == True:
    print('numbers_4 has a number that\'s not divisible by 3')