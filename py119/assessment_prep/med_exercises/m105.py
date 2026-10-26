"""
Write a function that takes a string as an argument and returns that string with
every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four',
'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit
character.

You may assume that the string does not contain any punctuation.

Inputs: string
Outputs: string

Explicit Rules:
- function returns the passed string but replaces every number word with its
  corresponding integer value

Implicit Rules:
- number words will be lowercase in the input string

Data Structure/s:
- string
- integer

Algorithm:
- set num_words to a dictionary where the keys are number words and the values
  are their corresponding integer representations as strings
- iterate through each num_word in num_words:
    - replace num_word in msg with num_words[num_word] and assign the result
      to msg
- return msg
"""


def word_to_digit(msg):
    num_words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for num_word in num_words:
        msg = msg.replace(num_word, num_words[num_word])
    return msg


message = "Please call me at five five five one two three four"
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
