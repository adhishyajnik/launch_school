"""
Inputs: integer
Outputs: integer

Explicit Rules:
- function returns the sum of all multiples of 7 and 11 that are less than
  the input integer
- if a number less than the input integer is a multiple of 7 and 11 (like 77),
  include it only once in the sum
- if the argument is 0, return 0

Implicit Rules:
- if the argument is less than 8, return 0
- if the argument is less than 12, return 7

Data Structure/s:
- integer
- set (to include multiples of both 7 and 11 only once)

Algorithm:
- set multiples to an empty set
- if input_int is less than 7, return 0
- set range_end to the integer division of input_int and 7
- iterate through each factor a range starting at 1 and ending at range_end + 1:
    - if 7 * factor is less than input_int, add 7 * factor to multiples
    - if 11 * factor is less than input_int, add 11 * factor to multiples
- return the sum of multiples
"""


def seven_eleven(input_int):
    multiples = set()
    if input_int < 7:
        return 0
    range_end = input_int // 7
    for factor in range(1, range_end + 1):
        if 7 * factor < input_int:
            multiples.add(7 * factor)
        if 11 * factor < input_int:
            multiples.add(11 * factor)
    return sum(multiples)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
