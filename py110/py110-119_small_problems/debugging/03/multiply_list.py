def multiply_list_buggy(lst):
    for item in lst:
        item *= 2

    return lst


print(multiply_list_buggy([1, 2, 3]) == [2, 4, 6])

"""
Because item evaluates to an integer from the list, line 3 tries to perform augmented multiplication on an integer rather than a variable that can store that result.

Consequently, the result of item * 2 does not get reassigned to the list element.

To solve this, we can either initialize an empty result list before the loop and append item * 2 to result on each iteration,

or we can iterate through the index and value of the enumerated list, and use the index values to perform indexed reassignment.

We can also do this with a list comprehension.
"""


def multiply_list1(lst):
    result = []
    for item in lst:
        result.append(item * 2)

    return result


print(multiply_list1([1, 2, 3]) == [2, 4, 6])


def multiply_list2(lst):
    for idx, item in enumerate(lst):
        lst[idx] = item * 2

    return lst


print(multiply_list2([1, 2, 3]) == [2, 4, 6])


def multiply_list3(lst):
    return [num * 2 for num in lst]


print(multiply_list3([1, 2, 3]) == [2, 4, 6])
