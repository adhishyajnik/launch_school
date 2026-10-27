"""
Inputs: string of integers
Outputs: integer

Explicit Rules:
- Function returns the number of even-numbered substrings in string of any
  length, including overlapping substrings
- If a substring occurs more than once, count both separately

Implicit Rules:
- Function will always be passed a non-empty string
- Function will always be passed a valid string of integers only

Data Structure/s:
- string
- integer

Algorithm:
- set count to 0
- iterate through each start_index in a range ending at the string length - 1:
    - iterate through each end_index in a range starting at 1 and ending at
      string length:
        - convert the slice of string from start_index to end_index to an integer
        - if that integer's modulus with 2 is 0:
            - increment count by 1
- return count
"""


def even_substrings(string):
    return len(
        [
            string[start_index:end_index]
            for start_index in range(len(string))
            for end_index in range(1, len(string) + 1)
            if string[start_index:end_index]
            and int(string[start_index:end_index]) % 2 == 0
        ]
    )


print(even_substrings("1432") == 6)
print(even_substrings("3145926") == 16)
print(even_substrings("2718281") == 16)
print(even_substrings("13579") == 0)
print(even_substrings("143232") == 12)
