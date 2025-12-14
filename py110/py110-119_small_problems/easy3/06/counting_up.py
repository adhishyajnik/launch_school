"""
Inputs: number (integer)
Outputs: list

Explicit Rules:
- Function returns list of all integers from 1 to 'number' inclusive, in ascending order
- Argument will always be a positive integer

Implicit Rules:
- Inputting 1 will return [1]

Algorithm:
- return a range from 1 to 'number' + 1, converted to a list
"""


def sequence(number):
    return list(range(1, number + 1))


print(sequence(5) == [1, 2, 3, 4, 5])  # True
print(sequence(3) == [1, 2, 3])  # True
print(sequence(1) == [1])  # True
