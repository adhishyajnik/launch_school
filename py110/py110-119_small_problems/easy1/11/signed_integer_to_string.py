"""
Inputs: positive or negative integer
Outputs: string

Explicit Rules:
- Function takes a positive or negative integer and returns its string representation
- Standard Python conversion functions like str are not to be used
- integer_to_string from the previous exercise may be used

Implicit Rules:
- non-zero positive and negative numbers should result in strings with a leading + or - sign respectively
- passing 0 to the function returns "0" without any sign

Data Structure/s:
- List to store the string representations of numbers at the same indices

Algorithm:
- get the absolute value of 'input_integer', set it to 'abs_val'
- pass 'abs_val' to 'integer_to_string' function, set result to 'unsigned'
- if 'input_integer' is less than zero
    - return "-" concatenated to 'unsigned'
- else if 'input_integer' is greater than zero
    - return "+" concatenated to 'unsigned'
- else
    - return "0"
"""

DIGITS = list("0123456789")


def integer_to_string(integer_value):
    output_string = ""

    while integer_value > 0:
        integer_value, remainder = divmod(integer_value, 10)
        output_string = DIGITS[remainder] + output_string

    return output_string or "0"


# My solution:
def my_signed_integer_to_string(signed_integer):
    abs_val = abs(signed_integer)
    unsigned = integer_to_string(abs_val)
    if signed_integer < 0:
        return "-" + unsigned
    elif signed_integer > 0:
        return "+" + unsigned
    return "0"


# Launch School Solution:
def signed_integer_to_string(signed_integer):
    if signed_integer < 0:
        return f"-{integer_to_string(-signed_integer)}"
    elif signed_integer > 0:
        return f"+{integer_to_string(signed_integer)}"
    return "0"


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")  # True
print(signed_integer_to_string(0) == "0")  # True
