"""
Inputs: 2 strings
Outputs: integer

Explicit Rules:
- Function returns the number of non-overlapping instances of substring
  in string; e.g. 'babab' contains 'bab' only once for the purposes of this
  function
- Assume that the second argument is never an empty string

Implicit Rules:
- If string is empty, return 0
- If string contains no instances of substring, return 0

Data Structure/s:
- string

Algorithm:
- return string.count(substring)
"""


def count_substrings(string, substring):
    return string.count(substring)


print(count_substrings("babab", "bab") == 1)
print(count_substrings("babab", "ba") == 2)
print(count_substrings("babab", "b") == 3)
print(count_substrings("babab", "x") == 0)
print(count_substrings("babab", "x") == 0)
print(count_substrings("", "x") == 0)
print(count_substrings("bbbaabbbbaab", "baab") == 2)
print(count_substrings("bbbaabbbbaab", "bbaab") == 2)
print(count_substrings("bbbaabbbbaabb", "bbbaabb") == 1)
