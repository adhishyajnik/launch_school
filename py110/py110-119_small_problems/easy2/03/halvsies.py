"""
Inputs: list
Outputs: a list containing two lists

Explicit Rules:
- Function returns a list containing 2 sub-lists
    the first half of input list elements are in sub-list 1 (inclusive of middle elements in odd-length lists)
    the second half of input list elements are in sub-list 2

Implicit Rules:
- If the input list has a single element, it will go in sub-list 1 and sub-list 2 will be empty
- If the input list is empty, the output list will contain 2 empty sub-lists

- Data Structure/s:
- input list
- output list with 2 sub-lists

Algorithm:
- initialize output to an empty list
- find the middle index of input_list
- append the slice of input_list from the beginning through the middle element to output
- append the slice of input_list from after the middle element through the end to output
- return output

Sub-algorithms:
Find the middle index of input_list
- odd numbered lists have the same midpoint index as lists with 1 more element
- the midpoint index of even numbered lists is simply half the length of the list
- list length modulo 2 is 1 for odd numbers and 0 for even numbers
- if we add input_list length to input_list length modulo 2
    then halve the sum, we get the midpoint index of any length list

list length     mid-point (slice stop)
1               1
2               1
3               2
4               2
5               3
6               3
"""


def halvsies(input_list):
    output = []
    mid = (len(input_list) + (len(input_list) % 2)) // 2
    output.append(input_list[:mid])
    output.append(input_list[mid:])
    return output


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
