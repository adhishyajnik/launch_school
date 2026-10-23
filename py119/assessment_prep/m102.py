"""
Write a function that rotates the last count digits of a number. To perform the
rotation, move the first of the digits that you want to rotate to the end and
shift the remaining digits to the left.

Inputs: 2 integers
Ouputs: integer

Explicit Rules:
- Function must be passed two integer arguments
- First argument is the number to be altered, second is the number of digits
  at the end of the number that the rotation is performed on
- The rotation applied to the last 'count' digits moves the first digit of that
  chunk to the end, and shifts the others to the right (exactly like the
  rotate_list function we already wrote)

Implicit Rules:
- Assume the function will never be passed fewer than 2 arguments
- Assume both arguments will be valid integers
- Assume count will never be longer than the number of digits in number

Data Structure/s:
- Integer
- List
- String

Algorithm:
- convert number to a string and then to a list, which will have each digit
  as a separate string element in the list (digit_list)
- set start_index to the length of digit_list minus count
- pass the slice of digit_list from start_index to the end to rotate_list()
  and bind its return value to rotated_digits
- while the length of digit_list is greater than start_index:
    - delete the last element from digit_list
- add rotated_digits to digit_list using augmented assignment (so the result is
  bound to digit_list)
- use str.join() to join all the digits in digit_list to a single string without
  any string separator, and then return the resulting string converted to an
  integer.
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


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)  # True
