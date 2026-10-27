"""
Inputs: list
Outputs: integer

Explicit Rules:
- Function returns the number of unique pairs of integers in the input list
- If the list is empty or length 1, return 0
- If there are no pairs, return 0

Implicit Rules:
- if an integer in the list is part of a pair, it cannot be part of another
  pair; e.g. [2, 2, 2] only has 1 pair, because the first pair of 2s excludes
  them from being used in another pair, leaving the last 2 in the list without
  another 2 to pair with

Data Structure/s:
- list

Algorithm:
- if length of lst is less than or equal to 1, return 0
- convert lst to a set to remove duplicates and then convert back to unique_lst
- set pairs to 0
- iterate through each num in unique_list:
    - count the number of nums in lst
    - add the integer quotient of the count and 2 to pairs
- return pairs
"""


def pairs(lst):
    if len(lst) <= 1:
        return 0
    unique_lst = list(set(lst))
    pairs = 0
    for num in unique_lst:
        pairs += lst.count(num) // 2
    return pairs


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
