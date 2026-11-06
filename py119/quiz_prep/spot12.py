"""
Inputs: list of strings
Outputs: list of integers

Explicit Rules:
- Function returns a list of integers
- Each integer corresponds to the word in string_list at the same index
- Each integer represents the number of letters in the corresponding string
  whose alphabets are in the same position as their order in the alphabet
  i.e. a is the first position, so if the string starts with a, the count
  increased by 1. If 'b' is the second letter in the string, count increases
  by 1 again.

Implicit Rules:
- function is case-insensitive, but helper function is meant for lowercase
  characters
- if no words contain letters in their alphabet positions, the returned list
  contains as many 0's as there are words in the input list
- an empty string in input list results in a 0 at the same index in the returned
  list

Data Structure/s:
- list
- string
- integer

Algorithm:
- lower_strings is the comprehension that transforms all the input strings
  to lowercase
- output_list = []
- iterate through each word in lower_strings:
    - count = 0
    - iterate through each index and char in enumerated word:
        - if index + 1 is the same as letter_position(char):
            - increment count by 1
    - append count to output_list
- return output_list
"""


def letter_position(letter):
    return ord(letter) - 96


# print(letter_position("a")) # returns 1
# print(letter_position("z")) # returns 26


def count_letters_in_position(string_list):
    lower_strings = [word.lower() for word in string_list]
    output_list = []
    for word in lower_strings:
        count = 0
        for idx, char in enumerate(word):
            if idx + 1 == letter_position(char):
                count += 1
        output_list.append(count)
    return output_list


# The below tests should each print True.
print(count_letters_in_position(["abode", "ABc", "xyzD"]) == [4, 3, 1])
print(count_letters_in_position(["abide", "ABc", "xyz"]) == [4, 3, 0])
print(count_letters_in_position(["IAM", "CODING", "HELP"]) == [0, 0, 0])
print(count_letters_in_position(["", "a", "b", "c"]) == [0, 1, 0, 0])
