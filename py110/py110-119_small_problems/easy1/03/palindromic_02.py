"""
Inputs: string
Outputs: boolean

Explicit Rules:
- Function must return True if input string is a palindrome, and False if it is not
- Palindromes read the same forwards and backwards
- Palindromes are case insensitive this time
- All non-alphanumeric characters should be ignored
    - "Madam" is a palindrome
    - "Madam, I'm Adam" is a palindrome
    - "356653" is a palindrome
    - "356635" is not a palindrome

Data Structure/s:
- We can use string.casefold() to make all characters the same case
- We can iterate through the input string one character at a time
- We can use string.replace() to remove any non-alphanumeric characters
- We should be able to use strings all the way through

Algorithm:
- convert alphanumeric string to the same case (str.casefold())
- iterate through the transformed input string one character at a time
    - if the current character is not alphanumeric, replace it with ""
- pass the transformed string to the is_palindrome function and return its result
    - reverse the transformed string using slicing and a step of -1
    - compare whether the transformed string is equal to its reverse
    - return the boolean result of the comparison
"""


def is_palindrome(input_string):
    return input_string == input_string[::-1]


def is_real_palindrome(input_string):
    input_string = input_string.casefold()
    for char in input_string:
        if not char.isalnum():
            input_string = input_string.replace(char, "")

    return is_palindrome(input_string)


print(is_real_palindrome("madam") == True)  # True
print(is_real_palindrome("356653") == True)  # True
print(is_real_palindrome("356635") == False)  # True
print(is_real_palindrome("356a653") == True)  # True
print(is_real_palindrome("123ab321") == False)  # True

# case doesn't matter
print(is_real_palindrome("Madam") == True)  # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True)  # True
