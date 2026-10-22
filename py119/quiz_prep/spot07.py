"""
Write a function that takes a list of words and constructs a new word by
concatenating the nth letter from each word, where n is the position of the word
in the list. Ignore if the nth letter from the word does not exist.

Input: list of strings
Output: string

Explicit Rules:
- function concatenates the character at the same string index as the current
  string's list index, assuming that list index exists in the string

Implicit Rules:

Data Structure/s:
- list
- string
- integers (indices)

Algorithm:
- initialize output_str to an empty string
- iterate through each str, idx in the enumerated input_lst:
    - if idx is less than the length of str:
        - add str[idx] to output_str
- return output_str
"""


def nth_char(input_lst):
    output_str = ""
    for idx, str in enumerate(input_lst):
        if idx < len(str):
            output_str += str[idx]
    return output_str


print(nth_char(["yoda", "best", "has"]))  # 'yes'
print(nth_char(["hello", "hello", "hello", "hello", "hello", "no"]))  # 'hello'
