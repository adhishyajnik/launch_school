"""
A merge sort is a recursive sorting algorithm that works by breaking down a
list's elements into nested sub-lists, then combining those nested sub-lists
back together in sorted order. It is best explained with an example. Given the
list [9, 5, 7, 1, 8, 2, 0, 6], let's walk through the process of sorting it with
merge sort. We'll start off by breaking the list down into nested sub-lists:

    - [9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
    - [[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
    - [[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
    - # repeat until each sub-list contains only 1 value
    - [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

In the first step, we partition the list into a list of two sub-lists, so that
each sub-list contains approximately half of the entries. In the next step, we
partition each sub-list in the same way. This process repeats until each of the
innermost lists contains exactly one element.

We now work our way back to a flat list by merging each pair of nested sub-lists
in the proper ascending order:

    - [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
    - [[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
    - [[2, 6, 7, 9], [0, 1, 5, 8]] -->
    - [0, 1, 2, 5, 6, 7, 8, 9]

For example, on the 2nd line, we merge [2, 9] with [6, 7], which becomes [2, 6,
7, 9].

Write a function that takes a list argument and returns a new list that contains
the values from the input list in sorted order. The function should sort the
list using the merge sort algorithm as described above. You may assume that
every element of the list will have the same data type: either all numbers or
all strings.

Feel free to use the merge function you wrote in the previous exercise.

Inputs: list
Outputs: sorted list

Explicit Rules:
- Function must use the merge sort method
- Breaking up elements of input list must be done by halving the size of
  each sublist repeatedly until the innermost lists only contain 1 element each
- Merging the list also happens in chunks of two innermost list elements at a
  time, and each merge also sorts the merged elements

Implicit Rules:
- Input list may not be a multiple of 2
- Input list may contain all integers or all strings
- Output list must be a new list; don't mutate the input list
- Output list must have no nested lists

Data Structure/s:
- list
- int
- str

Algorithm:
- slice the input list from the start to the halfway point, and from the halfway
  point to the end, and nest those two slices inside a list
- repeat the above for each sublist until every innermost list contains 1 elem
- using our custom merge function, merge the elements of the 2nd-innermost lists
- repeat the above for each outer list until the list has no nested lists
- return the resulting list

Sub-algos:
Split list elements into nested sublists until innermost lists contain 1 elem
- integer divide the length of the lst by 2, assign the result to halfway
- assign lst to a list containing
    - this function called on lst slice from start to halfway
    - this function called on lst slice from halfway to end
- return lst

Merge list elements starting with innermost, and progressing outward until the
resulting list has no more nested lists
- assign lst to a list containing
    - this function called on lst[0]
    - this function called on lst[1]
- return lst
"""


def case_insensitive(elem):
    return str(elem).casefold()


def recursive_split(lst):
    halfway = len(lst) // 2
    if halfway:
        lst = [recursive_split(lst[:halfway]), recursive_split(lst[halfway:])]
    return lst


def merge_list(lst1, lst2):
    ordered, unordered = [], [*lst1, *lst2]
    while unordered:
        if isinstance(unordered[0], str):
            min_elem = min(unordered, key=case_insensitive)
        else:
            min_elem = min(unordered)
        min_idx = unordered.index(min_elem)
        ordered.append(unordered.pop(min_idx))
    del unordered
    return ordered


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    splist1 = merge_sort(lst[: len(lst) // 2])
    splist2 = merge_sort(lst[len(lst) // 2 :])

    return merge_list(splist1, splist2)


"""
merge_sort([9, 5, 7, 1])
if len(lst) == 1:  # False

sub_list1 = lst[: len(lst) // 2]  # [9, 5]
sub_list2 = lst[len(lst) // 2 :]  # [7, 1]

sub_list1 = merge_sort(sub_list1)
            if len(sub_list1) == 1:  # False
            
            sub_list1 = sub_list1[: len(sub_list1) // 2]  # [9]
            sub_list2 = sub_list2[len(sub_list2) // 2 :]  # [5]

            sub_list1 = merge_sort(sub_list1)
                        if len(sub_list1) == 1:  # True
                            return sub_list1
                        [9]
            sub_list2 = merge_sort(sub_list2)
                        if len(sub_list2) == 1:  # True
                            return sub_list2
                        [5]
            
            return merge_list(sub_list1, sub_list2)
            [5, 9]
sub_list2 = merge_sort(sub_list2)
            if len(sub_list2) == 1:  # False
            
            sub_list1 = sub_list1[: len(sub_list1) // 2]  # [7]
            sub_list2 = sub_list2[len(sub_list2) // 2 :]  # [1]

            sub_list1 = merge_sort(sub_list1)
                        if len(sub_list1) == 1:  # True
                            return sub_list1
                        [7]
            sub_list2 = merge_sort(sub_list2)
                        if len(sub_list2) == 1:  # True
                            return sub_list2
                        [1]
            
            return merge_list(sub_list1, sub_list2)
            [1, 7]

return merge_list(sub_list1, sub_list2)
       merge_list([5, 9], [7, 1])
       [1, 5, 7, 9]
"""


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ["Sue", "Pete", "Alice", "Tyler", "Rachel", "Kim", "Bonnie"]
expected = ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)
