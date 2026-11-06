# UNFINISHED

"""
Inputs: string
Outputs: list of strings or an empty list

Explicit Rules:
- Function returns the top 3 most occurring words in a list
- Words in the list are organized in descending order
- Words include alphabetic characters and optionally apostrophes
- Ties can be broken arbitrarily
- Matches should be case insensitive
- If there are fewer than 3 unique words, return a list with the top 1 or top 2
- If the input string is empty, return an empty list

Implicit Rules:
- word boundaries are space characters
- periods and commas are not included in words
- a single apostrophe or a string of consecutive apostrophes are not a word

Data Structure/s:
- string
- list
- set

Algorithm:
- if input_str is empty, return []
- transform input_str to lowercase/casefold
- remove commas and periods
- split the string into a list at every space character, word_list
- iterate through word_list and remove any strings that don't contain any
  alphabets
- convert word_list to a set and back to a list, unique_words
- create an empty list, counts
- iterate through each word in unique_words:
    - count the number of instances of word in word_list and append that integer
      to counts (storing word counts in the same order as in unique_words)
- create an empty list, top3

- iterate through each _ in a range from 0 to 3:
    - if counts still has values:
        - find the maximum value in counts
        - find the index of the maximum value in counts
        - pop the count at that index
        - pop the word from unique_words at that popped index
          and add it to the start of top 3
- return top3
"""


def top_3_words(input_str):
    if input_str == "":
        return []

    lower_string = input_str.casefold()
    lower_string.replace(",", "")
    lower_string.replace(".", "")

    word_list = lower_string.split()

    word_list = [word for word in word_list for char in word if char.isalpha()]

    unique_words = list(set(word_list))

    counts = []
    for word in unique_words:
        counts.append(word_list.count(word))

    top3 = []
    for _ in range(3):
        if counts:
            max_val = max(counts)
            max_idx = counts.index(max_val)
            counts.remove(counts[max_idx])
            top3.insert(0, unique_words.pop(max_idx))

    return top3


print(top_3_words(" , e .. "))  # ["e"]
print(top_3_words(" ... "))  # []
print(top_3_words(" ' "))  # []
print(top_3_words(" ''' "))  # []
print(
    top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")  # should return ["a", "of", "on"]
)
