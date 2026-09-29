"""
A Rational Number is any number that can be represented as the result of the
division between two integers, e.g., 1/3, 3/2, 22/7, etc. The number to the left
is called the numerator, and the number to the right is called the denominator.

A Unit Fraction is a rational number where the numerator is 1.

An Egyptian Fraction is the sum of a series of distinct unit fractions (no two
are the same), such as:

-       1   1    1    1
-       - + - + -- + --
-       2   3   13   15

Every positive rational number can be written as an Egyptian fraction. For
example:

-           1   1   1   1
-       2 = - + - + - + -
-           1   2   3   6

Write two functions:

1. An egyptian() function that takes a Rational number as an argument, and
returns a list of the denominators that are part of an Egyptian Fraction
representation of the number.

2. An unegyptian() function that takes a list of numbers in the same format, and
calculates the resulting Rational number. You will need to use the Fraction
class provided by the fractions module.

EGYPTIAN FUNCTION:
==================
Inputs: rational number as a fraction object
Outputs: list of denominators of unit fractions whose sum is the input number

Explicit Rules:
- an Egyptian fraction is a series of unique unit fractions that sum to a
  positive rational number
- there are an infinite number of ways to represent a rational number as an
  Egyptian fraction, so our results may differ from the examples
- utilize the Fraction function from the fractions module

Implicit Rules:
- rational numbers are simply numbers that can be expressed as a ratio of two
  integers; they are not necessarily whole numbers, although all whole numbers
  are rational
- The Fraction object takes two integer arguments: numerator and denominator.
  If only one argument is passed, that becomes the numerator, and the
  denominator is 1 (i.e. Fraction(n) = n)
- 0 cannot be a denominator
- all numerators are 1

Data Structure/s:
- fraction
- int
- list

Algorithm:
- if rational number has 1 for a numerator:
    return a list containing its denominator
- set d to 1 and denominators to an empty list
- while True:
    - while 1/d is greater than rational number:
        - increment d by 1
    # this inner loop ensures we're always
    # subtracting a smaller number from a larger one

    - append d to denominators
    - set rational number to rational number minus 1/d
    - reduce rational number to its lowest common denominator
        # Fraction function does this automatically
    - if rational number is now a unit fraction
      and its denominator is not in denominators:
        - append rational number's denominator to denominators
          and return the list
    - increment d by 1
"""

from fractions import Fraction


def egyptian(rational):
    if rational.numerator == 1:
        return [rational.denominator]

    d, denominators = 1, []
    while True:
        while Fraction(1, d) > rational:
            d += 1
        denominators += [d]
        rational -= Fraction(1, d)
        if rational.numerator == 1 and rational.denominator not in denominators:
            return denominators + [rational.denominator]
        d += 1


def unegyptian(denominators):
    return sum([Fraction(1, d) for d in denominators])


# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))  # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))  # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]


# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
