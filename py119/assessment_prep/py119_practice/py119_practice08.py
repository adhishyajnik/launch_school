"""
Inputs: non-empty string
Outputs: integer

Explicit Rules:
- Passed string contains only lowercase alphabets, no empty strings passed
- Function returns length of the longest substring consisting only of vowels
- Vowels include a, e, i, o, and u

Implicit Rules:
- If there are no vowels in the passed string, return 0

Data Structure/s:
- string

Algorithm:
- set constant VOWELS to 'aeiou'
- longest = 0
- current = 0
- iterate through each char in string:
    - if char in vowels:
        - increment current_vowel_substring by 1
    - else:
        - set longest_vowel_substring to the max value between itself and
          current_vowel_substring
        - reset current_vowel_substring to 0
- return longest_vowel_substring
"""

VOWELS = "aeiou"


def longest_vowel_substring(string):
    longest, current = 0, 0
    for char in string:
        if char in VOWELS:
            current += 1
        else:
            longest = max(longest, current)
            current = 0
    longest = max(longest, current)
    return longest


print(longest_vowel_substring("cwm") == 0)
print(longest_vowel_substring("many") == 1)
print(longest_vowel_substring("launchschoolstudents") == 2)
print(longest_vowel_substring("eau") == 3)
print(longest_vowel_substring("beauteous") == 3)
print(longest_vowel_substring("sequoia") == 4)
print(longest_vowel_substring("miaoued") == 5)
