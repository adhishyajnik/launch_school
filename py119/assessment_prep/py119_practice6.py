"""
Inputs: string
Outputs: dict

Explicit Rules:
- Function returns a dictionary where the keys are the lowercase letters in the
  string, and the values are the frequency of that letter in string

Implicit Rules:
- order of keys in dictionary should match the order of unique lowercase
  letters in string; e.g. 'abac' should return {'a': 2, 'b': 1, 'c': 1}
    'a' key should not come after 'b' key even though there's an 'a' after the
    'b'
- function should accept strings containing alphabetic, punctuation and space
  chars
- if function is passed a string with no lowercase letters, output is an empty
  dictionary

Data Structure/s:
- string
- dict
"""


def count_letters(string):
    return {char: string.count(char) for char in string if char.islower()}


expected = {"w": 1, "o": 2, "e": 3, "b": 1, "g": 1, "n": 1}
print(count_letters("woebegone") == expected)

expected = {
    "l": 1,
    "o": 1,
    "w": 1,
    "e": 4,
    "r": 2,
    "c": 2,
    "a": 2,
    "s": 2,
    "u": 1,
    "p": 2,
}
print(count_letters("lowercase/uppercase") == expected)

expected = {"u": 1, "o": 1, "i": 1, "s": 1}
print(count_letters("W. E. B. Du Bois") == expected)

print(count_letters("x") == {"x": 1})
print(count_letters("") == {})
print(count_letters("!!!") == {})
