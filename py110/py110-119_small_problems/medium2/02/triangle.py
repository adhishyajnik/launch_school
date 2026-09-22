"""
A triangle is classified as follows:

    - Equilateral: All three sides have the same length.
    - Isosceles: Two sides have the same length, while the third is different.
    - Scalene: All three sides have different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides must be
greater than the length of the longest side, and every side must have a length
greater than 0. If either of these conditions is not satisfied, the triangle is
invalid.

Write a function that takes the lengths of the three sides of a triangle as
arguments and returns one of the following four strings representing the
triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

Inputs: 3 numbers (ints and/or floats)
Outputs: string

Explicit Rules:
- a valid triangle has 3 non-zero side-lengths, where the sum of the 2 shortest
  side-lengths is greater than the third side-length
- function returns type of triangle as a string ('equilateral', 'isosceles'.
  'scalene'), or 'invalid'
- equilateral triangles have 3 sides of equal length
- isosceles trianlges have 2 sides of equal length
- scalene triangles have 0 sides of equal length

Implicit Rules:
- Actually, for any valid triangle, the sum of any 2 side-lengths must be
  greater than the 3rd side-length, but its fastest to add the 2 shortest side-
  lengths to avoid having to check 3 different arithmetic operations
- arguments can be ints and floats
- each argument is the length of one side of a triangle
- floats will only be passed if there is a non-zero decimal component
- input will always be 3 numeric arguments greater than or equal to 0

Data Structure/s:
- int
- float
- set

Algorithm:
- put s1, s2, and s3 in a set
- if 0 is in the set, return 'invalid'
- if the length of the set is 1, return 'equilateral'
- else if the length of the set is 2, return 'isosceles'
- else:
    - sum the set members and then subtract the max value in the set
    - if the result is positive, return 'scalene'
"""


def triangle(*sides):
    if (0 in sides) or (sum(sides) - max(sides) <= max(sides)):
        return "invalid"
    elif len(set(sides)) == 1:
        return "equilateral"
    elif len(set(sides)) == 2:
        return "isosceles"
    else:
        return "scalene"


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")  # True
print(triangle(0, 3, 3) == "invalid")  # True
print(triangle(3, 1, 1) == "invalid")  # True
print(triangle(3, 1, 2) == "invalid")  # True
