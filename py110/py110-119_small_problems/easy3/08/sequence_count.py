"""
Inputs: count (integer), start_val (integer)
Outputs: list

Explicit Rules:
- Function returns a list of integers the length of 'count'
    - each element is a successive multiple of 'start_val' beginning with 'start_val' * 1
- 'count' will always be greater than or equal to 0
- If 'count' is 0, the function returns an empty list

Implicit Rules:
- 'start_val' can be positive, negative, or 0

Data Structure/s:
- count integer
- start_val integer
- list or list comprehension

Algorithm:
- initialize 'output' to an empty list
- iterate through each 'idx' in a range that stops at 'count'
    - append 'start_val' * ('idx' + 1) to 'output'
- return 'output'

As a list comprehension:
    Select: 'start_val' * ('idx' + 1)
    Collection Element: 'idx'
    Collection: a range that stops at 'count'
    Condition: none
"""


def sequence2(count, start_val):
    output = []
    for idx in range(count):
        output.append(start_val * (idx + 1))
    return output


def sequence(count, start_val):
    return [start_val * (idx + 1) for idx in range(count)]


print(sequence(5, 1) == [1, 2, 3, 4, 5])  # True
print(sequence(4, -7) == [-7, -14, -21, -28])  # True
print(sequence(3, 0) == [0, 0, 0])  # True
print(sequence(0, 1000000) == [])  # True
