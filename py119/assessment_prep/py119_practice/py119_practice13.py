"""
Inputs: two strings
Outputs: boolean

Explicit Rules:
- Function returns True if any portion of the characters in the first string
  can be used to form the second string, otherwise False
- assume both input strings are non-empty
- assume both input strings contain only lowercase alphabets

Implicit Rules:
- if a character is repeated in string 2, that character must also occur more
  than once in string 1 (checking for membership is not sufficient)

Data Structure/s:
- string
- list

Algorithm:
- convert scrambled to a list, scrambled_list
- iterate through each letter in target:
    - if letter is in scrambled_list:
        - remove letter from scrambled_list
    - else:
        - return False
- return True
"""


def unscramble(scrambled, target):
    scrambled_list = list(scrambled)
    for letter in target:
        if letter in scrambled_list:
            scrambled_list.remove(letter)
        else:
            return False
    return True


print(unscramble("ansucchlohlo", "launchschool") == True)
print(unscramble("phyarunstole", "pythonrules") == True)
print(unscramble("phyarunstola", "pythonrules") == False)
print(unscramble("boldface", "coal") == True)
print(unscramble("olc", "cool") == False)
