"""
Inputs: a string of digits
Outputs: an integer

Explicit Rules:
- the function converts a string of digits to an integer
- standard conversion functions like int may not be used
- function must calculate the result based on the string characters
- all string characters will be numeric; no +, -, or other non-digit characters

Implicit Rules:
- all strings will contain integers, no floats

Data Structure/s:
- input string
- output integer
- dictionary of integer values of digit strings

Algorithm:
- initialize a dictionary 'conversions':
    each key is a digit from 0-9 as a string
    each value is a digit from 0-9 as an integer
- initialize 'length' as the length of the input string
- initialize 'number' as 0
- iterate through each 'char' in 'input_string'
    - initialize 'cur_int' as the value of 'char' in the 'conversions' dictionary
    - decrement length by 1
    - initialize 'expanded' to the product of 'cur_int' and 10 ^ length
    - add 'expanded' to 'number'
- return 'number'
"""


def string_to_integer(int_string):
    CONVERSIONS = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    length = len(int_string)
    number = 0

    for char in int_string:
        cur_int = CONVERSIONS[char]
        length -= 1
        expanded = cur_int * (10**length)
        number += expanded
    return number
