"""
Write a function that takes a lowercase string as input and returns the length
of the longest substring that consists entirely of vowels (a, e, i, o, u).

Input: string
Output: integer

Explicit Rules:
- function returns the length of the longest consecutive run of vowels in
  input_string
- vowels include a, e, i, o, and u
- input is a lowercase string (case-sensitivity is not important)

Implicit Rules:
- if there are no vowels in input_string, return 0

Data Structure/s:
- string
- integer

Algorithm:
- define constant VOWELS as 'aeiou'
- initialize run_length to 0
- initialize longest_run to 0
- iterate through each char in input_string:
    - if char is any of the characters in VOWELS:
        - increment run_length by 1
    - else:
        - if longest_run is less than run_length:
            longest_run = run_length
        - run_length = 0
- return longest_run


"""

VOWELS = "aeiou"


def solve(input_string):
    run_length, longest_run = 0, 0
    for char in input_string:
        if char in VOWELS:
            run_length += 1
            longest_run = max(run_length, longest_run)
        else:
            run_length = 0
    return longest_run


print(solve("roadwarriors"))  # 2
print(solve("suoidea"))  # 3
