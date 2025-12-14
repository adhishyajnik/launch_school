"""
Inputs: int_input
Outputs: integer

Explicit Rules:
- Function returns 'int_input' as an integer with the digits reversed
- Argument is always a positive integer

Implicit Rules:
- Single digit inputs will output the same number as the input
- Inputs with trailing zeroes will not have those zeroes present in the output

Data Structure/s:
- int_input integer
- string in order to use reversed function
- list in order to capture result of reversed function
- output integer

Algorithm:
- initialize 'flipped' to 'int_input' converted to a string, reversed, and the result captured to a list
- initialize 'output' to 'flipped' joined to a single list with no joining characters
- return 'output' converted to an integer

OR

- use slicing with a -1 step to reverse the string version of 'int_input' and then convert it back to an integer and return it
"""


def reverse_number(int_input):
    flipped = list(reversed(str(int_input)))
    output = "".join(flipped)
    return int(output)


def reverse_number2(int_input):
    return int(str(int_input)[::-1])


print(reverse_number(12345) == 54321)  # True
print(reverse_number(12213) == 31221)  # True
print(reverse_number(456) == 654)  # True
print(reverse_number(1) == 1)  # True
print(reverse_number(12000) == 21)  # True
