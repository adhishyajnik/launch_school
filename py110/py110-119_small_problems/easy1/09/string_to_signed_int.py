"""
Inputs: string of digits that may or may not contain a leading + or - sign
Outputs: integer

Explicit Rules:
- Function takes a string of digits and returns the number as an integer
- String can have a leading + or -, or may not
- If the sign is -, the resulting integer should be negative
- If the sign is + or there is no sign, the resulting integer should be positive
- Every input string will contain a valid number
- Standard Python conversion functions like int are not to be used
- string_to_integer function from previous exercise may be used

Implicit Rules:
- The output integer should only have a sign if the number is negative
    - Positive integers don't have a leading + sign

Data Structure/s:
- string input
- dictionary in the string_to_integer function

Algorithm:
- if input_string starts with "-", initialize 'sign' to -1, otherwise initialize 'sign' to 1
- if the first character of input_string is not a digit, remove it from the string
- pass the resulting string to string_to_integer and multiply the result by 'sign'; store the product in 'integer_output'
- return 'integer_output'
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


def string_to_signed_integer(signed_int_string):
    sign = -1 if signed_int_string.startswith("-") else 1

    if signed_int_string.isdigit():
        stripped = signed_int_string
    else:
        stripped = signed_int_string[1:]

    output_integer = string_to_integer(stripped) * sign
    return output_integer


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)  # True
