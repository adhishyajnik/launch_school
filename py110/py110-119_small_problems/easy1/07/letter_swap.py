"""
Inputs: a string of space-separated words
Outputs: a string

Explicit Rules:
- function returns a string where each word's first and last letters are swapped
- every word contains at least 1 letter
- the string always contains at least 1 word
- strings only contain words and spaces
- strings do not have any leading, trailing, or repeated spaces

Implicit Rules:
- the function should preserve the case of the letters that are swapped:
    - "Hi" becomes "iH"
- single-character words don't change

Data Structure/s:
- List: split the input string into a list of words
- String for the input and the output

Algorithm:
- initalize an empty list 'swapped_words'
- split the input string into a list of words separated at each space character, 'words'
- iterate through each 'word' in 'words'
    - store the first letter of 'word' in 'first'
    - if 'word' is longer than 1 character, store the last letter of 'word' in 'last', otherwise 'last' is an empty string
    - concatenate 'last' + the slice of word excluding the first and last characters + 'first', store it as 'swapped'
    - append 'swapped' to 'swapped_words'
- join 'swapped_words' into a single string separated by spaces, 'output_string'
- return 'output_string'
"""


def swap(input_string):
    swapped_words = []
    words = input_string.split()
    for word in words:
        first = word[0]
        last = word[-1] if len(word) > 1 else ""
        swapped = last + word[1 : len(word) - 1] + first
        swapped_words.append(swapped)
    output_string = " ".join(swapped_words)
    return output_string


print(swap("Oh what a wonderful day it is") == "hO thaw a londerfuw yad ti si")  # True
print(swap("Abcde") == "ebcdA")  # True
print(swap("a") == "a")  # True
