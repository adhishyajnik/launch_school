"""
Write a function that takes a list of integers as input and counts the number of
non-touching pairs in the list. A non-touching pair is defined as two equal
integers separated by some other integer/s.

Inputs: list
Outputs: int

Explicit Rules:
- Function counts and returns the number of non-touching pairs in the input list
- A non-touching pair is two equal integers that are not consecutive in the
  input list

Implicit Rules:
- Non-touching pairs can re-use integers used in other non-touching pairs,
  e.g. [1, 2, 3, 2, 2] input would have 2 non-touching pairs (index 1 & 3 and
  index 1 & 4)

Data Structure/s:
- list
- int

Algorithm:
- initialize pairs to 0
- iterate through each idx in a range the length of the list:
    - iterate through each nidx in a range from idx + 2 to the length of the list:
        - if list[idx] == list[nidx]:
            - increment pairs by 1
- return pairs
"""


def non_touching_pairs(lst):
    pairs = 0
    length = len(lst)
    for idx in range(length):
        for nidx in range(idx + 2, length):
            if lst[idx] == lst[nidx]:
                pairs += 1
    return pairs


print(non_touching_pairs([1, 2, 5, 6, 5, 2]))
print(non_touching_pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]))
