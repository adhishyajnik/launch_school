"""
Write a function that rotates the LAST count digits of a number.
To perform the rotation, move the first of the digits that you
want to rotate to the end and shift the other digits to the left.

Inputs: int, int
Outputs: int

Explicit Rules:
- The first int argument is the int to be rotated (input)
- The second int argument is the number of digits to
  perform the rotation on (count)

Implicit Rules:
- Return value is an integer
- Assume the function will only receive valid integer inputs
- Assume the second argument will be less than the string length
  of the first argument (i.e. we will never rotate the entire input)

Data Structure/s:
- int
- str

Algorithm:
- coerce input to a string and assign to str_input
- the length of str_input minus count will be the start index
  of the rotated slice; we'll assign this integer to start
- assign the slice of str_input from start to the end to target
- concatenate the slice in str_input from 0 to start with
  the slice of target from index 1 to the end, and
  the first element of target
    assign this to rotated
- coerve rotated back to an int and return it
"""


def rotate_string(input):
    return input[1:] + input[0]


def rotate_rightmost_digits(input, count):
    str_input = str(input)
    start = len(str_input) - count
    target = str_input[start:]
    rotated = str_input[:start] + rotate_string(target)
    return int(rotated)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)  # True
