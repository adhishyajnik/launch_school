"""
Inputs: str_input (string)
Output: string

Explicit Rules:
- Function returns a string where each character from 'str_input' is doubled

Implicit Rules:
- Repeated characters have the same case
- Space and special characters are also repeated
- An empty string input returns an empty string

Data Structure/s:
- str_input string
- list to process letters one by one / for a list comprehension
- output string

Algorithm:
- return the joined string of elements of the following list comprehension:
    - double every 'char' in 'str_input'
"""


def repeater(str_input):
    return "".join([char * 2 for char in str_input])


print(repeater("Hello") == "HHeelllloo")  # True
print(repeater("Good job!") == "GGoooodd  jjoobb!!")  # True
print(repeater("") == "")  # True
