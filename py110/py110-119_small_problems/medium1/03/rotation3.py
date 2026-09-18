"""
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to
get 329175. Keep the first two digits fixed in place and rotate again to get
321759. Keep the first three digits fixed in place and rotate again to get
321597. Finally, keep the first four digits fixed in place and rotate the final
two digits to get 321579. The resulting number is called the maximum rotation
of the original number.

Write a function that takes an integer as an argument and returns the maximum
rotation of that integer. You can (and probably should) use the
rotate_rightmost_digits function from the previous exercise.

Inputs: int
Outputs: int

Explicit Rules:
- function returns the maximum rotation of input integer:
    - first rotation moves 1st digit of integer to the end
    - second rotation moves 2nd digit of resulting integer to the end
    - third rotation moves 3rd digit of resulting integer to the end
    - function keeps rotating the resulting integer this way until it reaches the
      2nd-last integer. Once this is complete, this is the maximum rotation of the
      integer.

Implicit Rules:
- single digit input integers will be output as is
- the last digit doesn't need to be rotated; stop after rotating 2nd-last digit
- if the maximum rotation of a number has a leading zero or zeroes, the function
  will return that integer without the leading zero/es.
- Assume the function will only be passed valid integer values

Data Structure/s:
- int
- str

Algorithm:
- coerce input to a string and assign it to str_input
- if the length of str_input is 1, return input
- loop through a range backwards from the length of str_input to 1
  with the loop variable count:
    - call rotate_rightmost_digits on str_input, count
        - modify rotate_rightmost_digits to output a string, not int
    - assign the result of the function call back to str_input

- coerce str_input back to an integer and return it
"""


def rotate_string(input):
    return input[1:] + input[0]


def rotate_rightmost_digits(input, count):
    str_input = str(input)
    start = len(str_input) - count
    target = str_input[start:]
    rotated = str_input[:start] + rotate_string(target)
    return rotated


def max_rotation(input):
    str_input = str(input)
    if len(str_input) == 1:
        return input

    for count in range(len(str_input), 1, -1):
        str_input = rotate_rightmost_digits(str_input, count)

    return int(str_input)


# Test cases; all should return True

print(max_rotation(735291) == 321579)  # True
print(max_rotation(3) == 3)  # True
print(max_rotation(35) == 53)  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)  # True
