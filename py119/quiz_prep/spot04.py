"""
A pangram is a sentence that contains every single letter of the alphabet at
least once. Given a string, detect whether or not it is a pangram. Return True
if it is, False if not. Ignore numbers and punctuation.

Input: string
Output: bool

Explicit Rules:
- function returns True if input string is a pangram, False if not
- pangrams contain every letter of the alphabet at least once
- don't count numbers and punctuation, only characters from A-z

Implicit Rules:
- function is case-insensitive

Data Structure/s:
- string
- bool

Algorithm:
- coerce input_string to lowercase
- convert lowercase_string to a set (which collapses duplicate characters into
  unique members)
- if the length of the set is at least 26 (the length of the alphabet):
    return True
- return False

Backup algo:
- initialize alphabets to a string containing all lowercase letters
- iterate through each letter in alphabets:
    - if letter is in the lowercase-coerced input_string:
        continue
    - else:
        return False
- return True
"""

# CONSTANTS
ALPHABET_LENGTH = 26
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"


def pangram_set(input_string):
    lowercase_set = set(input_string.lower())
    if len(lowercase_set) >= ALPHABET_LENGTH:
        return True
    return False


def pangram(input_string):
    for letter in ALPHABETS:
        if letter in input_string.lower():
            continue
        else:
            return False
    return True


print(pangram("The quick brown fox jumps over the lazy dog."))  # True
print(pangram("This is not a pangram."))  # False
