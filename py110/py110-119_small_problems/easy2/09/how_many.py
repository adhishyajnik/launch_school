"""
Inputs: lst (list)
Outputs: 1 or more print statements

Explicit Rules:
- Function prints each unique element in 'lst' alongside its count
- Words are case sensitive
    'suv' is not the same as 'SUV'

Implicit Rules:
- Each element and its count are printed on a new line
- The order in which the elements/counts are printed does not matter
- Argument contains at least 1 element
- Elements are all strings

Data Structure/s:
- input list
- set (to reduce collection to unique elements if needed)
- integer count
- string/f-string

Algorithm:
- iterate through each 'elem' in 'lst' converted to a set
    - print an f-string with 'elem' and the number of instances of 'elem' in 'lst'
"""


def count_occurrences(lst):
    for elem in set(lst):
        print(f"{elem} => {lst.count(elem)}")


def further_exploration(lst):
    caseless = [elem.casefold() for elem in lst]
    for elem in set(caseless):
        if elem == "suv":
            print(f"{elem.upper()} => {caseless.count(elem)}")
        else:
            print(f"{elem.capitalize()} => {caseless.count(elem)}")


vehicles = [
    "car",
    "car",
    "truck",
    "car",
    "SUV",
    "truck",
    "motorcycle",
    "motorcycle",
    "car",
    "truck",
]

case_insensitive = [
    "car",
    "Car",
    "truck",
    "car",
    "SUV",
    "TRUCK",
    "MOTORCYCLE",
    "motorcycle",
    "CAR",
    "Truck",
]

count_occurrences(vehicles)

further_exploration(case_insensitive)
