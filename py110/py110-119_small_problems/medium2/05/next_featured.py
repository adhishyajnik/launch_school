"""
A featured number (something unique to this exercise) is an odd number that is a
multiple of 7, with all of its digits occurring exactly once each. For example,
49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a
multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next
featured number greater than the integer. Issue an error message if there is no
next featured number.

NOTE: The largest possible featured number is 9876543201.

Inputs: integer
Outputs: integer or string

Explicit Rules:
- a featured number is:
    - odd
    - a multiple of 7
    - a number whose digits are all unique
- function takes any integer as an argument, returns the next featured number or
  the error message: There is no possible number that fulfills those
  requirements.


Implicit Rules:
- there are no featured numbers greater than 9876543201
    - the function should immediately return an error if the
      passed integer is greater than that
- only positive integers will be passed to the function

Data Structure/s:
- int
- str
- set

Algorithm:
- initialize MAX_FEATURED to 9876543201 as a constant
- initialize ERR_MSG to "There is no possible number that fulfills those
  requirements."
- if the passed integer is greater than MAX_FEATURED, return ERR_MSG
- find the next multiple of 7 greater than the passed integer
- while multiple is less than or equal to MAX_FEATURED:
    - if the multiple is odd:
        - if all the digits are unique, return the number
    - increment multiple by 7

Sub-algos:
Find the next multiple of 7 greater than the passed integer
- get the modulus of the passed integer and 7
- subtract the modulus from 7 and add the result to the passed integer
- return the result

Check if all digits of the passed integer are unique
- convert the passed integer to a string, then a set
- if the length of the set is equal to the length of the string, return True
- return False
"""


def digits_unique(integer):
    numstr = str(integer)
    return True if len(set(numstr)) == len(numstr) else False


def next_odd_mult_of_7(integer):
    next_mult = (7 - (integer % 7)) + integer
    return next_mult if next_mult % 2 != 0 else next_mult + 7


def next_featured(integer):
    MAX_FEATURED = 9876543201
    ERR_MSG = "There is no possible number that fulfills those requirements."

    if integer >= MAX_FEATURED:
        return ERR_MSG

    mult = next_odd_mult_of_7(integer)
    while mult < MAX_FEATURED:
        if digits_unique(mult):
            return mult
        mult += 14

    return MAX_FEATURED


def next_featured_2(integer):  # this version runs significantly slower
    MAX_FEATURED = 9876543201
    ERR_MSG = "There is no possible number that fulfills those requirements."

    next_mult = (7 - (integer % 7)) + integer
    next_mult = next_mult if next_mult % 2 != 0 else next_mult + 7

    for mult in range(next_mult, MAX_FEATURED + 1, 14):
        if len(set(str(next_mult))) == len(str(next_mult)):
            return next_mult

    return ERR_MSG


print(next_featured(12) == 21)  # True
print(next_featured(20) == 21)  # True
print(next_featured(21) == 35)  # True
print(next_featured(997) == 1029)  # True
print(next_featured(1029) == 1043)  # True
print(next_featured(999999) == 1023547)  # True
print(next_featured(999999987) == 1023456987)  # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = "There is no possible number that fulfills those requirements."
print(next_featured(9876543201) == error)  # True
