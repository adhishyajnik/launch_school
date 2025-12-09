"""
Inputs: a string of zero or more space-separated words
Outputs: a dictionary that shows the number of words of different sizes

Explicit Rules:
- the output dictionary keys are integers representing each unique word length in the input string
    - values are integers representing the number of words of that length contained in the input string
- non-alphabetic characters do not contribute to word length

Implicit Rules:
- an empty input string returns an empty dictionary
- non-space characters are not included in word lengths, including numbers and special characters
- dictionary keys must be unique
- input strings won't contain sequences of space characters; each space character will be surrounded by non-space characters

Data Structure/s:
- list: we can use string.split() to create a list of words in the input string
- we need an output dictionary

Algorithm:
- initialize an empty dictionary, 'output_dict'
- split the input string into a list of words separated at each space character, 'words'
- iterate through each 'word' in 'words'
    - initialize 'length' to 0
    - iterate through each 'char' in 'word':
        - if 'char' is alphabetic, increment 'length' by 1
    - if 'length' is not a key in 'output_dict', add it as a new key and set its value to 0
    - increment the value associated with that key by 1
- return 'output_dict'
"""


def word_sizes(input_string):
    output_dict = {}
    words = input_string.split()

    for word in words:
        length = 0
        for char in word:
            if char.isalpha():
                length += 1

        if length not in output_dict:
            output_dict[length] = 0

        output_dict[length] += 1

    return output_dict


# All of these examples should print True

string = "Four score and seven."
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = "Hey diddle diddle, the cat and the fiddle!"
print(word_sizes(string) == {3: 5, 6: 3})

string = "Humpty Dumpty sat on a w@ll"
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes("") == {})
