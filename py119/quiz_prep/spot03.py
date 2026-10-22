"""
Write a function that takes two strings as input, full_text and search_text, and
returns the number of times search_text appears in full_text.

Inputs: two strings
Outputs: integer

Explicit Rules:
- inputs must be strings
- must have two inputs
- the function searches full_text for the substring search_text, rather than
  searching for the characters in search_text individually

Implicit Rules:
- input strings must have at least 1 character each
- case is not important (assume all strings are lowercase)
- the function will never return negative values
- if search_text is not found in full_text, 0 is returned
- multiple instances of search_text may overlap within full_text; each instance
  counts as an occurrence of search_text

Data Structure/s:
- strings
- integers

Algorithm:
- initialize count to 0
- initialize search_len to the number of characters in search_text
- iterate through each idx in a range the length of full_text:
    - if the chunk of letters from idx to idx + search_len matches search_text:
        - increment count by 1
"""


def solution(full_text, search_text):
    count, search_len = 0, len(search_text)
    for idx in range(len(full_text)):
        if full_text[idx : idx + search_len] == search_text:
            count += 1
    return count


print(solution("abcdeb", "b"))  # 2
print(solution("aaabbbcccc", "bbb"))  # 1
print(solution("aaabbbbcccc", "bbb"))  # 2
