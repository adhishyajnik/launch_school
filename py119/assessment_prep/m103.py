"""
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to get
329175. Keep the first two digits fixed in place and rotate again to get 321759.
Keep the first three digits fixed in place and rotate again to get 321597.
Finally, keep the first four digits fixed in place and rotate the final two
digits to get 321579. The resulting number is called the maximum rotation of the
original number.

Write a function that takes an integer as an argument and returns the maximum
rotation of that integer. You can (and probably should) use the
rotate_rightmost_digits function from the previous exercise.

Inputs: integer
Outputs: integer

Explicit Rules:
- Maximum rotation rotates the full passed integer,
  then everything but the first digit
  then everything but the first 2 digits
  ...
  and finally just the last two digits of the passed integer

Implicit Rules:
- max-rotated numbers that end up having leading zeroes will get omitted
  when we return the final integer version of the number, and that's ok
- the function should not convert the number to an integer until all the
  rotations are completed

Algorithm:
- get the number of digits (num_digits) by counting the length of the
  number converted to a string (num_string)
- iterate through each digit in a range the length of num_digits:
    - set rcount to num_digits minus digit
    - call rotate_rightmost_digits on (num_string, rcount) and assign the return
      value to num_string
        - we'll need to modify this function so it works on a string
          for the number argument, and also returns a string
- return num_string converted to an integer
"""


def rotate_list(lst):
    if lst == []:
        return []
    elif isinstance(lst, list) == False:
        return None

    output = lst[1:]
    output.append(lst[0])
    return output


def rotate_rightmost_digits(number, count):
    digit_list = list(str(number))
    start_index = len(digit_list) - count
    rotated_digits = rotate_list(digit_list[start_index:])
    while len(digit_list) > start_index:
        del digit_list[-1]
    digit_list += rotated_digits
    return int("".join(digit_list))


def max_rotation(number):
    num_string = str(number)
    num_digits = len(num_string)
    for digit in range(num_digits):
        rcount = num_digits - digit
        num_string = rotate_rightmost_digits(num_string, rcount)
    return int(num_string)


print(max_rotation(735291) == 321579)  # True
print(max_rotation(3) == 3)  # True
print(max_rotation(35) == 53)  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)  # True
