"""
Inputs: string
Outputs: boolean

Explicit Rules:
- function returns True if input string is a pangram, False if not
- a pangram contains each letter of the alphabet at least once
- function is case-insensitive

Implicit Rules:
- assume the function will only be passed a valid string

Data Structure/s:
- string

Algorithm:
- define a constant ALPHABETS as a string containing all the letters of the
  alphabet
- iterate through each letter in ALPHABETS:
    - if letter is not in the lowercase version of the string, return False
- return True
"""

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(string):
    for letter in ALPHABETS:
        if letter not in string.casefold():
            return False
    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!") == True)
print(is_pangram("The slow, brown fox jumps over the lazy dog!") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = "Sixty zippers were quickly picked from the woven jute bag."
print(is_pangram(my_str) == True)
