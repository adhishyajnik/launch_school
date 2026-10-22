"""
Write a function that takes a string of integers as input and returns the number
of substrings that result in an odd number when converted to an integer.

Inputs: string of integers
Outputs: integer

Explicit Rules:
- function returns the number of substrings that are odd numbers
- input is a string of integers with no other character types but digits 0-9

Implicit Rules:
- odd substrings can overlap; all count
- return 0 if there are no odd substrings

Data Structure/s:
- strings
- integers
- range

Algorithm:
- odd_subs = 0
- iterate through each sub_len in a range the length of int_str:
    - iterate through each num in int_str:
        - if int(int_str[num to num + sub_len]) modulo 2 is 1:
            - increment odd_subs by 1
- return odd_subs
"""


def solve(int_str):
    odd_subs = 0
    for sub_len in range(1, len(int_str) + 1):
        for idx in range(len(int_str)):
            cur_sub = int_str[idx : idx + sub_len]
            if len(cur_sub) == sub_len:
                if int(int_str[idx : idx + sub_len]) % 2 == 1:
                    odd_subs += 1
    return odd_subs


print(solve("1341"))  # 7
print(solve("1357"))  # 10
