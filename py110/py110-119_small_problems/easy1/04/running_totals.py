"""
Inputs: list of numbers
Outputs: list of numbers

Explicit Rules:
- function takes a list of numbers and returns a list of the same length,
    where each number is the running total of the input list

Implicit Rules:
- each number in the output list is the sum of all of the numbers
    up to and including the number at that index from the input list
- numbers in input and output lists are all positive integers
- input list can be of any length, including an empty list
- an empty input list returns an empty output list
- a list with a single number returns the same list

Data Structure/s:
- input will be a list of integers
- output will be a list of integers
- no need for any other data types

Algorithm:
- initialize an empty output list 'output_list'
- iterate through a range the length of the input list 'num_list'
    - slice 'num_list' from the beginning up to and including the number at the index of the current range value
    - sum all the numbers in that slice
    - append the sum to 'output_list'
- return 'output_list'
"""


def running_total(num_list):
    output_list = []
    for i in range(len(num_list)):
        output_list.append(sum(num_list[: (i + 1)]))
    return output_list


print(running_total([2, 5, 13]) == [2, 7, 20])  # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])  # True
print(running_total([3]) == [3])  # True
print(running_total([]) == [])  # True
