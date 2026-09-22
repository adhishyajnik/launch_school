"""
Write a function that takes a string and returns a dictionary containing the
following three properties:

    - the percentage of characters in the string that are lowercase letters
    - the percentage of characters that are uppercase letters
    - the percentage of characters that are neither

All three percentages should be returned as strings whose numeric values lie
between "0.00" and "100.00", respectively. Each value should be rounded to two
decimal points.

You may assume that the string will always contain at least one character.

Inputs: string
Outputs: dictionary

Explicit Rules:
- input string can contain uppercase, lowercase, and non-alphabetic characters
- keys in returned dictionary are 'lowercase', 'uppercase', and 'neither'
- the values in the returned dictionary are string-coerced floats with
  2 decimal places, between 0.00 and 100.00
- if a percentage value has 0 or 1 decimal value, pad out to 2 decimal places:
  '5.00' instead of '5.0', and '56.90' instead of '56.9'

Implicit Rules:
- input string will contain at least 1 character
- input will always be a string

Data Structure/s:
- str
- dict
- float

Algorithm:
- get the number of characters in str_input and assign that to length
- initialize three variables to 0: lower, upper, and nthr
- loop through each character in str_input
    - if char is lowercase, increment lower
    - elif char is uppercase, increment upper
    - else increment nthr
- calculate the percentages of each type of character, rounded to 2 decimals
  and coerced to a string
- generate a dictionary of each type of character and its percentages

Sub-algos:

"""


def calculate_percent(number, length):
    return f"{((number / length) * 100):.2f}"


def letter_percentages(str_input):
    total_chars = len(str_input)

    l_lets = len([char for char in str_input if char.islower()])
    u_lets = len([char for char in str_input if char.isupper()])
    n_lets = total_chars - l_lets - u_lets

    return {
        "lowercase": calculate_percent(l_lets, total_chars),
        "uppercase": calculate_percent(u_lets, total_chars),
        "neither": calculate_percent(n_lets, total_chars),
    }


expected_result = {
    "lowercase": "50.00",
    "uppercase": "10.00",
    "neither": "40.00",
}
print(letter_percentages("abCdef 123") == expected_result)

expected_result = {
    "lowercase": "37.50",
    "uppercase": "37.50",
    "neither": "25.00",
}
print(letter_percentages("AbCd +Ef") == expected_result)

expected_result = {
    "lowercase": "0.00",
    "uppercase": "0.00",
    "neither": "100.00",
}
print(letter_percentages("123") == expected_result)


"""
length = 100
print(calculate_percent(5))  # "5.00"
print(calculate_percent(37.59))  # "37.59"
print(calculate_percent(0))  # "0.00"
print(calculate_percent(100))  # "100.00"
"""

"""
print(kwargs_to_dict(lowercase="5.67", uppercase="47.50", neither="46.67"))
"""
