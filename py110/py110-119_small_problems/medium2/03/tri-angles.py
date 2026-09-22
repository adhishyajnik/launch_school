"""
A triangle is classified as follows:

    - Right: One angle is a right angle (exactly 90 degrees).
    - Acute: All three angles are less than 90 degrees.
    - Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees, and
every angle must be greater than 0. If either of these conditions is not
satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and
returns one of the following four strings representing the triangle's
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry
about floating point errors. You may also assume that the arguments are in
degrees.

Inputs: three integers
Outputs: string

Explicit Rules:
- the sum of angles of any triangle is 180
- right triangle has 1 90-degree angle
- acute triangle has 3 angles less than 90 degrees
- obtuse triangle has 1 angle greater than 90 degrees
- no triangle has any angles that are 0
- function takes 3 angles and returns 'right', 'acute', 'obtuse', or 'invalid'

Implicit Rules:
- only integer values will be passed to the function
- arguments are in degrees

Data Structure/s:
- list
- integer
- string

Algorithm:
- if any of the angles is 0 or
  if the sum of the angles is not 180, return 'invalid'
- else if any of the angles is 90, return 'right'
- else if any of the angles is greater than 90, return 'obtuse'
- else return acute
"""


def triangle(*angles):
    if 0 in angles or sum(angles) != 180:
        return "invalid"
    elif max(angles) >= 90:
        return "right" if max(angles) == 90 else "obtuse"
    return "acute"


print(triangle(60, 70, 50) == "acute")  # True
print(triangle(30, 90, 60) == "right")  # True
print(triangle(120, 50, 10) == "obtuse")  # True
print(triangle(0, 90, 90) == "invalid")  # True
print(triangle(50, 50, 50) == "invalid")  # True
