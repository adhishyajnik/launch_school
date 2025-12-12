"""
Inputs: number (integer)
Outputs: list

Explicit Rules:
- Function returns a list of digits in 'number'
- 'number' is always positive

Implicit Rules:
- 'number' is always non-zero

Data Structure/s:
- integer
- string
- list

Algorithm:
- return a list comprehension:
    - the iterable is 'number' converted to a string
    - convert each character of the iterable to an integer
"""


def digit_list(number):
    return [int(elem) for elem in str(number)]


print(digit_list(12345) == [1, 2, 3, 4, 5])  # True
print(digit_list(7) == [7])  # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])  # True
print(digit_list(444) == [4, 4, 4])  # True
