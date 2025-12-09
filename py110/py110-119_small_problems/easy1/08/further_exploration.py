"""
Write a hexadecimal_to_integer function that converts a string
representing a hexadecimal number to its integer value.
Hexadecimal numbers use base 16 instead of 10, and the
characters A, B, C, D, E and F (and the lowercase equivalents)
correspond to decimal values of 10-15.


4d9f(hex)   = (f * 16^0) + (9 * 16^1) + (d * 16^2) + (4 * 16^3)
            = 15 + 144 + 3328 + 16384
            = 19871
"""


def hexadecimal_to_integer(hex_string):
    CONVERSIONS = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
    }

    value = 0
    position = 0
    for char in hex_string[::-1]:
        value += CONVERSIONS[char.casefold()] * (16**position)
        position += 1

    return value


print(hexadecimal_to_integer("4D9f") == 19871)  # True
