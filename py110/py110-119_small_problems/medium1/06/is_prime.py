"""
A prime number is a positive number that is evenly divisible only by itself and
1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not
prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the
number 1 is not prime.

Write a function that takes a positive integer as an argument and returns True
if the number is prime, False if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your
task is to programmatically determine whether a number is prime without relying
on functions that already do that for you.

Inputs: integer
Outputs: boolean

Explicit Rules:
- primes are divisible only by themselves and 1
- 1 is not prime
- return True if the passed integer is prime, False if not
- function will only be passed positive integers

Implicit Rules:
- 0 is not prime
- negative numbers are not prime
- even numbers greater than 2 are not prime
- numbers greater than 9 whose last digit is 5 are not prime
- numbers greater than 3 ending in a 3, 6, or 9 are not prime
- add the digits in number, then repeat for the resulting number until you're left with a 1-digit number.
    - if that number is 9, number is divisble by 9 and not prime
- no number has any factors greater than itself/2
- better yet: non-prime numbers will have at least one factor at or less than its square root

Data Structure/s:
- int
- str
- range
- bool

Algorithm:
- if integer is less than 2, return False
- if integer is greater than 2 and even, return False
- if integer is greater than 3 and ends with a 3, or 9, return False
- if integer is greater than 9 and ends with a 5, return False
- loop through a range from 1 to the integer
    - if the current range number is 2, 3, or 5, continue to the next loop iteration
    - if the modulus of the integer and the current range value is 0:
        - return False
- return True
"""

import math


def is_div_by_9(integer):
    int_list = [int(numstr) for numstr in list(str(integer))]
    digsum = 0
    while True:
        if len(int_list) == 1:
            return int_list[0] == 9
        for digit in int_list:
            digsum += digit
        int_list = [int(numstr) for numstr in list(str(digsum))]
        digsum = 0


def is_prime(integer):
    if (
        (integer < 2)
        or (integer > 2 and integer % 2 == 0)
        or (integer > 5 and str(integer)[-1] == "5")
    ):
        return False
    for factor in range(3, math.isqrt(integer) + 1):
        if integer % factor == 0:
            return False
    return True


"""
print(is_div_by_9(9))
print(is_div_by_9(18))
print(is_div_by_9(999))
print(is_div_by_9(9693))
"""


print(is_prime(1) == False)  # True
print(is_prime(2) == True)  # True
print(is_prime(3) == True)  # True
print(is_prime(4) == False)  # True
print(is_prime(5) == True)  # True
print(is_prime(6) == False)  # True
print(is_prime(7) == True)  # True
print(is_prime(8) == False)  # True
print(is_prime(9) == False)  # True
print(is_prime(10) == False)  # True
print(is_prime(23) == True)  # True
print(is_prime(24) == False)  # True
print(is_prime(997) == True)  # True
print(is_prime(998) == False)  # True
print(is_prime(3_297_061) == True)  # True
print(is_prime(23_297_061) == False)  # True
