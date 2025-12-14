"""
Inputs: str_input (string)
Outputs: string

Explicit Rules:
- Function returns a string where every consonant in 'str_input' is doubled
- No vowels, digits, punctuation, or whitespace should be doubled
- Vowels include 'a', 'e', 'i', 'o', and 'u,' case-insensitive
- Only ASCII characters will be included in the argument

Implicit Rules:
- An empty input string returns an empty output string
- Doubled characters are of the same case

Data Structure/s:
- str_input string
- string of all consonants
- string output

Algorithm:
- initialize a constant 'CONSONANTS', with all lowercase consonants
- initialize 'doubled' to an empty string
- iterate through each 'char' in 'str_input'
    - if the lowercase version of 'char' is in 'CONSONANTS', concatenate 'char * 2' to 'doubled'
    - otherwise concatenate 'char' to 'doubled'
return 'doubled'
"""

CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def double_consonants(str_input):
    doubled = ""
    for char in str_input:
        if char.lower() in CONSONANTS:
            doubled += char * 2
        else:
            doubled += char
    return doubled


# All of these examples should print True
print(double_consonants("String") == "SSttrrinngg")
print(double_consonants("Hello-World!") == "HHellllo-WWorrlldd!")
print(double_consonants("July 4th") == "JJullyy 4tthh")
print(double_consonants("") == "")
