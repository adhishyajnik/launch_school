"""
Inputs: string
Outputs: boolean

Explicit Rules:
- Function must return True if input string is a palindrome, and False if it is not
- Palindromes read the same forwards and backwards
- Case matters, and all characters matter
    - "Madam" is not a palindrome
    - "madam i'm adam" is not a palindrome
    - "356653" is a palindrome
Implicit Rules:
    - input string can include numbers and special characters

Data Structure/s: We should be able to use strings for all our operations

Algorithm:
- reverse the input string using slicing and a step of -1
- output the result of an equality comparison between input string and reversed string
"""


def is_palindrome(input_string):
    return input_string == input_string[::-1]


# All of these examples should print True

print(is_palindrome("madam") == True)
print(is_palindrome("356653") == True)
print(is_palindrome("356635") == False)

# case matters
print(is_palindrome("Madam") == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
