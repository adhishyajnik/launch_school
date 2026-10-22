"""
Write a function that takes a non-empty string s as input and finds the minimum
substring t and the maximum number k, such that the entire string s is equal to
t repeated k times.

Inputs: string
Outputs: list (first element string, second element integer)

Explicit Rules:
- Function returns a list where the string at index zero and the integer at
  index 1 multiplied together result in the input string
- String in the returned list must be the shortest possible string, and the
  integer in the returned list must be the highest value integer such that
  multiplying the string by the integer results in the input string

Implicit Rules:
- Function will never be passed an empty string or another object type
- The string in the returned list will never be empty
- The integer in the returned list will never be less than 1

Data Structure/s:
- string
- integer
- list

Algorithm:
- initialize input_length to the length of input_str
- initialize substring_length to 0
- while True:
    - increment substring_length by 1
    - set substring to the slice of input_str from 0 to substring_length
    - if input_length divided by substring_length has no remainder:
        - set factor to input_length divided by substring_length
    - else:
        - continue
    - if substring * factor is the input_str:
        - return the list [substring, factor]
"""


def smallest_repeated_substring(input_str):
    input_length = len(input_str)
    substring_length = 0
    while True:
        substring_length += 1
        substring = input_str[0:substring_length]
        if input_length % substring_length == 0:
            factor = input_length // substring_length
        else:
            continue
        if substring * factor == input_str:
            return [substring, factor]


print(smallest_repeated_substring("ababab"))  # ["ab", 3]
print(smallest_repeated_substring("aaaaaa"))  # ["a", 6]
print(smallest_repeated_substring("abcabcabc"))  # ["abc", 3]
print(smallest_repeated_substring("xyz"))  # ["xyz", 1]
print(smallest_repeated_substring("zzzzzzzzzz"))  # ["z", 10]
print(smallest_repeated_substring("ababababx"))  # ["ababababx", 1]
print(smallest_repeated_substring("abcdabcd"))  # ["abcd", 2]
print(smallest_repeated_substring("abaaba"))  # ["aba", 2]
print(smallest_repeated_substring("a"))  # ["a", 1]
