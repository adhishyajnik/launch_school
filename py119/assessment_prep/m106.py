"""
A prime number is a positive number that is evenly divisible only by itself and
1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not
prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the
number 1 is not prime.

Write a function that takes a positive integer as an argument and returns True
if the number is prime, False if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your task
is to programmatically determine whether a number is prime without relying on
functions that already do that for you.

Inputs: integer
Outputs: bool

Explicit Rules:
- function returns True if the passed integer is prime, False if not
- prime numbers are divisible only by 1 and themselves
- 1 is not prime because it is only divisible by 1 and no other unique number
- Don't use any Python add-ons to solve this

Implicit Rules:
- Assume function will only be passed valid positive integers

Data Structure/s:
- integer

Algorithm:
- if
    - integer is 1, or
    - integer is greater than 2 and is divisible by 2, or
    - integer is greater than 5 and its last digit is 5:
        - return False
- iterate through each factor a range starting at 3 and ending at integer // 2,
  with a step of 2 (i.e. skip even numbers)
    - if factor ends in a 5, continue
    - if number divided by factor has a remainder of 0, return False
- return True
"""


def is_prime(integer):
    if (
        (integer == 1)
        or (integer > 2 and str(integer)[-1] in "24680")  # even numbers
        or (integer > 5 and str(integer)[-1] == "5")  # multiples of 5
    ):
        return False
    for factor in range(3, integer // 2, 2):  # check only odd factors
        if str(factor)[-1] == "5":  # skip odd factors divisible by 5.
            continue
        if integer % factor == 0:
            return False
    return True


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
