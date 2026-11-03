"""
Inputs: string
Outputs: tuple with a string and an integer

Explicit Rules:
- Function returns a tuple with a string and an integer, such that the
  string is the shortest substring that if multiplied by the integer,
  results in the input string
- Function will only be passed a string of lowercase alphabets

Implicit Rules:
- If the integer component of the tuple is 1, the longest substring is
  the input string

Data Structure/s:
- string
- integer
- tuple

Algorithm:
- iterate through each end_index in a range ending at string length
    - current_substring is the slice of string from 0 to end index
    - if the length of the string modulus length of current_substring is 0:
        - current_integer is length of string // length of current_substring
        - if current_substring * current_integer == string:
            - return (current_substring, current_integer)
"""


def repeated_substring(string):
    for end_index in range(1, len(string) + 1):
        current_substring = string[:end_index]
        if len(string) % len(current_substring) == 0:
            current_integer = len(string) // len(current_substring)
            if current_substring * current_integer == string:
                return (current_substring, current_integer)


print(repeated_substring("xyzxyzxyz") == ("xyz", 3))
print(repeated_substring("xyxy") == ("xy", 2))
print(repeated_substring("xyz") == ("xyz", 1))
print(repeated_substring("aaaaaaaa") == ("a", 8))
print(repeated_substring("superduper") == ("superduper", 1))
