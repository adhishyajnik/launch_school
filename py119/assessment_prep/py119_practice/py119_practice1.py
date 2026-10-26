"""
Inputs: list of integers
Outputs: list of integers

Explicit Rules:
- For each number in lst, function counts the number of integers in the list of
  lesser value and returns a list of those numbers
- Function should only count unique values. E.g. if lst is [8, 1, 1],
  the returned list should be [1, 0, 0]

Implicit Rules:
- Assume that lst will be a valid list of integers of length 1 or greater
- Output list should be the same length as input list
- If the input list has a length of 1, the output list will only contain 0

Data Structure/s:
- List

Algorithm:
- set output_lst to []
- iterate through each num in lst:
    - set count to 0
    - iterate through each lesser_num range the length of num:
        - if lesser_num is in lst:
            - increment count by 1
    - append count to output_lst
- return output_lst

- iterate through each elem in lst:
    - count = len(set([num for num in lst if num < elem]))


"""


def smaller_numbers_than_current(lst):
    return [len(set([num for num in lst if num < elem])) for elem in lst]


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
