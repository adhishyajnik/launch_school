"""
Bubble Sort is one of the simplest sorting algorithms available. It is not an
efficient algorithm, so developers rarely use it in real code. However, it is an
excellent exercise for student developers. In this exercise, you will write a
function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On
each pass, the two values of each pair of consecutive elements are compared. If
the first value is greater than the second, the two elements are swapped. This
process is repeated until a complete pass is made without performing any swaps.
At that point, the list is completely sorted.

6 	2 	7 	1 	4 	Start: compare 6 > 2? Yes
2 	6 	7 	1 	4 	Swap
2 	6 	7 	1 	4 	6 > 7? No (no swap)
2 	6 	7 	1 	4 	7 > 1? Yes
2 	6 	1 	7 	4 	Swap
2 	6 	1 	7 	4 	7 > 4? Yes
2 	6 	1 	4 	7 	Swap

2 	6 	1 	4 	7 	2 > 6? No
2 	6 	1 	4 	7 	6 > 1? Yes
2 	1 	6 	4 	7 	Swap
2 	1 	6 	4 	7 	6 > 4? Yes
2 	1 	4 	6 	7 	Swap
2 	1 	4 	6 	7 	6 > 7? No

2 	1 	4 	6 	7 	2 > 1? Yes
1 	2 	4 	6 	7 	Swap
1 	2 	4 	6 	7 	2 > 4? No
1 	2 	4 	6 	7 	4 > 6? No
1 	2 	4 	6 	7 	6 > 7? No

1 	2 	4 	6 	7 	1 > 2? No
1 	2 	4 	6 	7 	2 > 4? No
1 	2 	4 	6 	7 	4 > 6? No
1 	2 	4 	6 	7 	6 > 7? No
1 	2 	4 	6 	7 	No swaps; all done; sorted

We can stop iterating the first time we make a pass through the list without
making any swaps since that means the entire list is sorted.

For further information -- including pseudo-code that demonstrates the
algorithm, as well as a minor optimization technique -- see the Bubble Sort
Wikipedia page.

Write a function that takes a list as an argument and sorts that list using the
bubble sort algorithm described above. The sorting should be done "in-place" --
that is, the function should mutate the list. You may assume that the list
contains at least two elements.

Inputs: list
Outputs: mutated input list sorted

Explicit Rules:
- bubble sort iterates through the list, comparing 2 consecutive elements at
  a time, and swapping their order if necessary. It iterates through the list
  as many times as it takes for no swaps to be made
- sort should be done in-place, i.e. by mutating the input list
- function returns the sorted list

Implicit Rules:
- input list will contain at least 2 elements
- input list will only contain 1 type of object
- input list may contain all integers or all strings
    - strings may be mixed case, so use str.casefold() before comparing
    - strings will only contain alphabetic characters
- the length of the sorted list should be the same as the original length
- don't use sorted() or list.sort()

Data Structure/s:
- list
- integers
- strings
- booleans

Algorithm:
- while True:
    - initialize swapped to False
    - loop through each num in a range from 0 to input_list length - 1
        - if the element at index num is greater than the element after it:
            - pop element at index num and insert it at the next index
            - or reassign element at idx to elem at idx + 1 and vice versa on
              on one line
            - set swapped to True
    - if swapped is False, return (the mutated) input_list
"""


def bubble_sort(lst):
    while True:
        sorting_complete = True
        for idx in range(len(lst) - 1):
            if str(lst[idx]).casefold() > str(lst[idx + 1]).casefold():
                lst.insert(idx + 1, lst.pop(idx))
                # lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                sorting_complete = False
        if sorting_complete:
            break


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])  # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])  # True

lst3 = ["Sue", "Pete", "Alice", "Tyler", "Rachel", "Kim", "Bonnie"]
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]
print(lst3 == expected)  # True

lst4 = ["Sue", "Sally", "alice", "Allan", "AListair", "Saul", "Salome"]
bubble_sort(lst4)

expected = ["alice", "AListair", "Allan", "Sally", "Salome", "Saul", "Sue"]
print(lst4 == expected)  # True
