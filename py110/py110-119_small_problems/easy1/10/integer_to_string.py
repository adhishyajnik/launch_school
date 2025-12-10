"""
Inputs: integer
Outputs: string

Explicit Rules:
- Function converts a non-negative integer to its string representation
- Standard Python conversion functions like str are not to be used
- Function must analyze and manipulate the number to construct the string
- 0 is a non-negative number

Implicit Rules:
- output strings do not need to contain a leading + sign
- input integers will obviously not include a leading + sign
- output strings do not need commas separating each thousands place

Data Structure/s:
- dictionary to convert digits 0-9 to their string representations
- input integer
- output string

Algorithm:
- initialize a dictionary 'CONVERSIONS'
    keys are digits 0-9 as integers
    values are digits 0-9 as strings

- initialize 'output_string' to an empty string
- start a loop (break condition specified in the block)
    - get the modulus of 'input_integer' and 10, set the result to 'cur_digit'
    - get the 'CONVERSIONS' dictionary value for 'cur_digit' and concatenate it with 'output_string', set the result to 'output_string'
    - if 'input_integer' is less than 10 (no more digits left to convert), break out of the loop
    - otherwise, subtract 'cur_digit' from 'input_integer' and divide the result by 10, set the result to 'integer_value'
- return 'output_string'
"""

CONVERSIONS = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
}

DIGITS = list("0123456789")


# My Solution:
def my_integer_to_string(integer_value):
    output_string = ""
    while True:
        cur_digit = integer_value % 10
        output_string = CONVERSIONS[cur_digit] + output_string
        if integer_value < 10:
            break
        integer_value = (integer_value - cur_digit) // 10

    return output_string


# Launch School Solution:
def integer_to_string(integer_value):
    output_string = ""

    while integer_value > 0:
        integer_value, remainder = divmod(integer_value, 10)
        output_string = DIGITS[remainder] + output_string

    return output_string or "0"


print(integer_to_string(4321) == "4321")  # True
print(integer_to_string(0) == "0")  # True
print(integer_to_string(5000) == "5000")  # True
print(integer_to_string(1234567890) == "1234567890")  # True
