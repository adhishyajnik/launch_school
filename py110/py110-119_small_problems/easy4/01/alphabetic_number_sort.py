"""
Inputs: list
Outputs: list

Explicit Rules:
- Argument is a list of integers from 0 - 19 inclusive of both
- Function returns a list of integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

Data Structure/s:
- list input, containing integers
- list output, containing integers

Algorithm:
- Return input_list sorted with a sort key that converts list items to their English word

Sub-Algorithm: convert any integer from 0 - 19 to its English word and return a string
Inputs: integer
Outputs: string
- Initialize num_words to dictionary where the key is an integer from 0 - 19 and the value is the English word for that number as a string
- Return the value of the input_integer key in num_words, which is a string
"""

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

NUM_WORDS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]


def englishify(int_value):
    return NUM_WORDS[int_value]


def alphabetic_number_sort(int_list):
    return sorted(int_list, key=englishify)


print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
