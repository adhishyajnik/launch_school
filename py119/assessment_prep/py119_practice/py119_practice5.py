"""
Inputs: string
Outputs: single character string

Explicit Rules:
- Function returns the character most used in string
- If multiple characters have the same frequency, function returns the character
  that occurs first in string
- Function should be case-insensitive

Implicit Rules:
- Assume function will only be passed strings of alphabetic characters,
  punctuation, and spaces -- no numeric characters
- Function should return an alphabetic character

Data Structure/s:
- string
- list?

Algorithm:
- letter_freq = dict()
- iterate through each char in string:
    - if char is not alphabetic:
        continue
    - letter_freq[char] = string.count(char)
- highest_freq = max(letter_freq.values())
- highest_idx = list(letter_freq.values()).index(highest_freq)
- return letter_freq.keys[highest_idx]
"""


def most_common_char(string):
    string = string.casefold()
    letter_freq = {
        char: string.count(char) for char in string if char.isalpha()
    }
    highest_freq = max(letter_freq.values())
    highest_idx = list(letter_freq.values()).index(highest_freq)
    return list(letter_freq.keys())[highest_idx]


print(most_common_char("Hello World") == "l")
print(most_common_char("Mississippi") == "i")
print(most_common_char("Happy birthday!") == "h")
print(most_common_char("aaaaaAAAA") == "a")

my_str = "Peter Piper picked a peck of pickled peppers."
print(most_common_char(my_str) == "p")

my_str = "Peter Piper repicked a peck of repickled peppers. He did!"
print(most_common_char(my_str) == "e")
