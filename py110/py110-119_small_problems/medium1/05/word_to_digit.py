"""
Write a function that takes a string as an argument and returns that string with
every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four',
'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit
character.

You may assume that the string does not contain any punctuation.

Inputs: string
Outputs: string

Explicit Rules:
- any number words in the input string are changed to their integer value
  (zero, one, two, three, four, five, etc.)
- input string will only contain alphanumeric characters and spaces, no punct

Implicit Rules:
- only number words from 0-9 will be part of input string; no negatives or
  2-digit numbers

Data Structure/s:
- string
- int
- list

Algorithm:
- initialize num_words to a dictionary where the key is the number word, and
  its value is the integer value as a string: {'zero': '0', 'one': '1', etc.}
- split str_input at each space and assign it to word_list
- initialize an empty string to str_output
- loop through each word in word_list:
    - if word is in num_words, get the dictionary value of word
      and append it to str_output
    - otherwise, append word to str_output
    - append a space character to str_output
- return str_output with the trailing spaces stripped
"""


def word_to_digit1(str_input):
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

    output_str = ""
    for word in str_input.split():
        if word in num_words:
            output_str += num_words[word]
        else:
            output_str += word
        output_str += " "

    return output_str.rstrip()


def word_to_digit2(str_input):
    NUM_WORDS = {
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

    word_list = str_input.split()
    return " ".join([NUM_WORDS.get(word, word) for word in word_list])


# test case
message = "Please call me at five five five one two three four"
print(word_to_digit2(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
