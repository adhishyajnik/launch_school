"""
Inputs: string of alphanumeric characters
Outputs: integer greater than or equal to 0

Explicit Rules:
- function returns the number of unique characters in input_string
  that occur more than once
- input_string contains only alphanumeric characters
- function is case-insensitive

Implicit Rules:
- if no characters in input_string occur more than once, return 0

Data Structure/s:
- string
- set
- int

Algorithm:
- set input_lower to the lowercase version of input_string
- set unique_chars to input_lower converted to a set, then converted to a list
- set repeats to 0
- iterate through each char in unique_chars:
    - if input_lower.count(char) is greater than 1:
        - increment repeats by 1
- return repeats
"""


def distinct_multiples(input_string):
    input_lower = input_string.lower()
    unique_chars = list(set(input_lower))
    repeats = 0
    for char in unique_chars:
        repeats += input_lower.count(char) > 1
    return repeats


print(distinct_multiples("xyz") == 0)  # (none)
print(distinct_multiples("xxyypzzr") == 3)  # x, y, z
print(distinct_multiples("xXyYpzZr") == 3)  # x, y, z
print(distinct_multiples("unununium") == 2)  # u, n
print(distinct_multiples("multiplicity") == 3)  # l, t, i
print(distinct_multiples("7657") == 1)  # 7
print(distinct_multiples("3141592653589793") == 4)  # 3, 1, 5, 9
print(distinct_multiples("2718281828459045") == 5)  # 2, 1, 8, 4, 5
