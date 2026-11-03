"""
Inputs: list of integers
Outputs: integer from the list

Explicit Rules:
- Function returns the integer in int_list that occurs an odd number of times
- int_list will always have one such integer

Implicit Rules:
- If int_list only has 1 element, return that element

Data Structure/s:
- list
- int

Algorithm:
- set unique_nums to int_list converted to a set and then to a list
- iterate through each num in unique_nums:
    - set ct to the number of occurrences of num in int_list
    - if ct is odd:
        return num
"""


def odd_fellow(int_list):
    unique_nums = list(set(int_list))
    for num in unique_nums:
        if int_list.count(num) % 2 == 1:
            return num


print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
