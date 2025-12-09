"""
Input:
    - List of strings
Output:
    - List of strings sorted by greatest number of adjacent consonants

Explicit Rules:
    - Consonants are adjacent if they are next to each other in the same word
    - Consonants are considered adjacent even if a space separates them
    - If two strings contain the same number of adjacent consonants, their
      relative order should be the same in the sorted list
Implicit Rules:
    - Strings can contain multiple words
    - Vowels include A, E, I, O, and U
    - Strings with a single consonant have 0 adjacent consonants
    - Strings with no consonant also have 0 adjacent consonants

Further notes/questions:
    - Can strings be empty?
        - Unresolved, no test cases included empty strings
    - Should the strings be sorted in ascending or descending order?
        - Descending order; greatest number of adjacent consonants first
    - Are adjacent consonants case-sensitive?
        - Unresolved, test cases include lowercase characters and spaces only
    - Do vowels include the letter Y?
        - No
    - Do strings include numbers or other special characters?
        - Unresolved, no test cases included empty strings
    - Are numbers and/or special characters ignored or considered non-consonant
      characters? How will we know the extension works?
        - Unresolved, no test cases included empty strings

Test Cases:
    - See below.

Data Structure/s:
    - List of strings as input, another list of strings as output
    - We might need a dictionary to assign adjacent consonant counts to each
      string, depending on implementation

Algorithm:
    1. Create a 'sorted' list to store our sorted strings
    2. Count the number of adjacent consonants in each string in the list - sub-algorithm below
    3. Add the string with the greatest number of adjacent consonants to 'sorted' - sub-algorithm below
    4. Repeat step 3 until the length of the input list and 'sorted' are the same
    5. Return the 'sorted' list

Sub-algorithms:

Count the number of adjacent consonants in each string in the list
    Input:
        - list of strings
    Output:
        - list of integers representing the maximum number of adjacent consonants in the string at the same index

    Examples:
        - Input: ["aa", "baa", "ccaa", "dddaa"]
            - Output: [0, 0, 2, 3]
        - Input: ["can can", "toucan", "batman", "salt pan"]
            - Output: [2, 0, 2, 3]
        - Input: ["bar", "car", "far", "jar"]
            - Output: [0, 0, 0, 0]
        - Input: ["day", "week", "month", "year"]
            - Output: [0, 0, 3, 0]
        - Input: ["xxxa", "xxxx", "xxxb"]
            - Output: [3, 4, 4]

    Algorithm:
        1. Define an empty list, 'counts'
        2. Count the maximum number of adjacent consonants in the first string - sub-algorithm below
        3. Append that count to the 'counts' list
        4. Repeat steps 2 and 3 for the rest of the strings in the list
        5. Return the 'counts' list

Count the number of adjacent consonants in a string
    Input:
        - string
    Output:
        - number of adjacent consonants in the string (integer)

    Data Structure/s:
        - set or frozen set to hold all consonant characters

    Examples:
        - Input: "dddaa"
            - Output: 3
        - Input: "can can"
            - Output: 2
        - Input: "bar"
            - Output: 0
        - Input: "aa"
            - Output: 0

    Algorithm:
        1. Define 'consonants' as the set of upper and lowercase characters excluding A, E, I, O, U, a, e, i, o, and u
        2: Remove all spaces from the string
        3: Define 'running_total' as -1
        4: Define 'longest_sequence' as 0
        5: Iterate through the string one character at a time:
            A. If the current character is in 'consonants', increment 'running_total' by 1
            B. Otherwise, if 'running_total' is greater than 'longest_sequence':
                1. Set 'longest_sequence' to 'running_total'
                2. Set 'running_total' to 0
        6: Return 'longest_sequence'

Add the string with the greatest number of adjacent consonants to the result list
    Input:
        - 'string_list'
        - 'counts' list of greatest number of adjacent consonants in each string
        - 'sorted' list
    Output:
        - None
    Side-Effects:
        - leftmost string with max number of adjacent consonants removed from 'string_list' and appended to 'sorted' list
        - the leftmost maximum integer is removed from 'counts'

    Data Structure/s:
        - Three lists as input, each get mutated

    Examples:
        - Input: ["aa", "baa", "ccaa", "dddaaa"], [0, 0, 2, 3], []
            - Side Effects:
                - string_list: ["aa", "baa", "ccaa"]
                - counts: [0, 0, 2]
                - sorted: ["dddaa"]
        - Input: ["can can", "toucan", "batman", "salt pan"], [2, 0, 2, 3], []
            - Side Effects:
                - string_list: ["can can", "toucan", "batman"]
                - counts: [2, 0, 2]
                - sorted: ["salt pan"]
        - Input: ["bar", "car", "far", "jar"], [0, 0, 0, 0], []
            - Side Effects:
                - string_list: ["car", "far", "jar"]
                - counts: [0, 0, 0]
                - sorted: ["bar"]
        - Input: ["day", "week", "month", "year"], [0, 0, 3, 0], []
            - Side Effects:
                - string_list: ["day", "week", "year"]
                - counts: [0, 0, 0]
                - sorted: ["month"]
        - Input: ["xxxa", "xxxx", "xxxb"], [3, 4, 4], []
            - Side Effects:
                - string_list: ["xxxa", "xxxb"]
                - counts: [3, 4]
                - sorted: ["xxxx"]

    Algorithm:
        1. Find the greatest value in the 'counts' list
        2. Get the index of the leftmost instance of that value
        3. Remove that element from 'counts'
        4. Get the string from 'string_list' at the same index
        5. Append that string to 'sorted' list
        6. Remove that string from 'string_list'
"""


def count_adj_consonants(string):
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    spaceless = "".join(string.split())
    running_total = 0
    longest_sequence = 0

    for char in spaceless:
        if char in consonants:
            running_total += 1
            if (running_total > 1) and (running_total > longest_sequence):
                longest_sequence = running_total
        else:
            running_total = 0

    return longest_sequence


def get_adj_consonant_counts(string_list):
    counts = []
    for string in string_list:
        counts.append(count_adj_consonants(string))
    return counts


def get_first_sort_string(string_list, counts):
    max_count = max(counts)
    first_max_index = counts.index(max_count)
    del counts[first_max_index]
    return string_list.pop(first_max_index)


def sort_by_consonant_count(string_list):
    sorted = []
    counts = get_adj_consonant_counts(string_list)  # this is a list of integers

    while string_list:
        sorted_string = get_first_sort_string(string_list, counts)
        sorted.append(sorted_string)

    return sorted


# Test Cases:
my_list = ["aa", "baa", "ccaa", "dddaa"]
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ["can can", "toucan", "batman", "salt pan"]
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ["bar", "car", "far", "jar"]
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ["day", "week", "month", "year"]
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ["xxxa", "xxxx", "xxxb"]
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
