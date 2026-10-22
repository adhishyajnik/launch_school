"""
Write a function that takes a string as input and counts the occurrences of each
lowercase letter in the string. Return the counts in a dictionary where the
letters are keys and their counts are values.

Inputs: string
Outputs: dict

Explicit Rules:
- each lowercase letter is a key in the returned dictionary
- the value of each key is the count of that letter in the input string

Implicit Rules:
- the function will only be passed strings

Data Structure/s:
- string
- dictionary

Algorithm:
- Initialize a new empty dictionary, output
- Iterate through the input string per character
- If the character is not a key in the output dictionary, add it with value 1
- If the character is already a key in the output dictionary, increment that
key's value by 1
- Return the output dictionary
"""


def letter_count(str):
    return {letter: str.count(letter) for letter in str}


print(
    letter_count("launchschool")
    == {
        "a": 1,
        "c": 2,
        "h": 2,
        "l": 2,
        "n": 1,
        "o": 2,
        "s": 1,
        "u": 1,
    }
)
# True
