"""
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

Inputs: list
Outputs: list

Explicit Rules:
- Function is passed a list of strings
- Function returns a list of the same string values with the vowels removed from each
- Vowels include a, e, i, o, and u

Implicit Rules:
- Uppercase and lowercase vowels should be removed
- If a string consists of vowels only, the function should transform it into an empty string
- The order of the characters in each string in the resulting list should be the same as in the original lists

Data Structure/s:
- list
- strings
- slicing

Algorithm:
- perform a comprehension that returns each string without vowels
    iterating over each string in input_list

Sub-algorithm: return input_string without vowels
- perform a list comprehension that returns the character
    iterating over each character in input_string
    if the character is not a vowel
"""

VOWELS = "AEIOUaeiou"


def trim_string(input_string, trim_chars):
    return "".join([char for char in input_string if char not in trim_chars])


def remove_vowels(lst):
    return [trim_string(str_val, VOWELS) for str_val in lst]


# All of these examples should print True
original = ["abcdefghijklmnopqrstuvwxyz"]
expected = ["bcdfghjklmnpqrstvwxyz"]
print(remove_vowels(original) == expected)  # True

original = ["green", "YELLOW", "black", "white"]
expected = ["grn", "YLLW", "blck", "wht"]
print(remove_vowels(original) == expected)  # True

original = ["ABC", "AEIOU", "XYZ"]
expected = ["BC", "", "XYZ"]
print(remove_vowels(original) == expected)  # True
