"""
Write a function that generates text following a pattern where:

    - the first and last characters of each word remain in their original place
    - characters between the first and last characters are sorted alphabetically
    - punctuation should remain at the same place as it started

Input: string (containing letters, punctuation, and spaces)
Output: string

Explicit Rules:
- function leaves the first and last letters of each word in the same position
- function sorts the remaining characters of each word alphabetically
- function preserves the position of all punctuation and spaces
- function returns the resulting string

Implicit Rules:
- letters in the input string are all lowercase

Data Structure/s:
- string
- list

Algorithm:
- split input_str into a wordlist separated at each space character
- iterate through each idx, word in the enumerated wordlist:
    - sort its inner letters of word (except punctuation)
      and leave its punctuation in place
    - replace the word at idx with the inner-sorted word
- join all the words in wordlist with a space

Sub-algorithm: inner_sort
- initialize punct_chars to a list of tuples of form (idx, char) for only
  the punctuation characters in str
- initialize alpha_chars to a list of only alphabetic characters in str
- assign sorted_list to a list containing (in order):
    - the first element of alpha_chars,
    - the inner elements of alpha_chars, sorted and unpacked
    - the last element of alpha_chars
- iterate through each punct_idx, punct in punct_chars:
    - insert the punct into sorted_list at punct_idx
- return sorted_list joined to a string with no separating characters
"""


def inner_sorted(str):
    punct_chars = [
        (idx, char) for idx, char in enumerate(str) if char.isalpha() == False
    ]
    alpha_chars = [char for char in str if char.isalpha()]

    sorted_list = [alpha_chars[0], *sorted(alpha_chars[1:-1]), alpha_chars[-1]]
    for punct_idx, punct in punct_chars:
        sorted_list.insert(punct_idx, punct)

    return "".join(sorted_list)


def scramble_words(input_str):
    wordlist = input_str.split(" ")
    for idx, word in enumerate(wordlist):
        wordlist[idx] = inner_sorted(word)
    return " ".join(wordlist)


# print(inner_sort("qlskfjghzd") == "qfghjklszd")
# print(inner_sort("qlsk'fjgh-zd") == "qfgh'jkls-zd")
# print(inner_sort("qlsk'fjgh-zd.") == "qfgh'jkls-zd.")


print(scramble_words("professionals") == "paefilnoorsss")
print(
    scramble_words(
        "you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."
    )
    == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."
)
