"""
A binary search is a much more efficient alternative to a linear search. This
algorithm lets you cut the search area in half on each iteration by discarding
the half that you know your search term doesn't exist in. The binary search
algorithm is able to do this by relying on the data being sorted. Going back to
the phone book example, let's say that we're searching the following phone_book
data for the search item 'Smith':

    - # Phone book data
    - phone_book = [
    -     'Embry',
    -     'Hanson',
    -     'Hawkins',
    -     'John',
    -     'Lee',
    -     'Seeli',
    -     'Smith',
    -     'Zimmer',
    - ]

With a linear search, we would have to sequentially go through each of the names
until we found the search item, 'Smith'. In a binary search, however, the
following sequence happens:

    - Retrieve the middle value from the data (assume truncation to integer) -->
      'John'.
    - If the middle value is equal to 'Smith', stop the search.
    - If the middle value is less than 'Smith':
        - Discard the lower half, including the middle value --> `['Embry',
          'Hanson', 'Hawkins', 'John'].
        - Repeat the process from the top, using the upper half as the starting
          data --> ['Lee', 'Seeli', 'Smith', 'Zimmer'].
    - If the middle value is greater than 'Smith', do the same as the previous
      step, but with opposite halves.

Using the process described above, the search successfully ends on the third
iteration when the middle value is 'Smith'. For an 8-element list like this, we
need, at most, 3 iterations. For an 8000-element list, we need, at most, just 13
iterations. For 8,000,000 elements, we need just 23 iterations. This is
incredibly efficient.

Implement a binary_search function that takes a list and a search item as
arguments, and returns the index of the search item if found, or -1 otherwise.
You may assume that the list argument will always be sorted.

Inputs: list of all ints or all strings
Outputs: integer

Explicit Rules:
- repeat the following recursively until the middle elem is the search target:
    - check the middle element of the collection:
        - if it's less than the search target, discard everything up to and
          including the middle element
        - if it's greater than the search target, discard everything after and
          including the middle element
- return the index of the found element, or -1 if not found

Implicit Rules:
- input lists will be sorted
- don't use list.index() method
- input list will contain only unique elements
- probably requires recursion

Data Structure/s:
- list
- int
- str
- dict to store index along with value?

Algorithm:
- if search isn't in iter, return -1
- get the approximate middle index of iter and assign it to midx
- if the iter object at midx is search:
    - return midx
- else if the iter object at midx is less than search:
    - add to midx: binary search the slice of iter from midx to the end
- else if the iter object at midx is greater than search:
    - assign midx: binary search the slice of iter from the beginning to midx
- return midx
"""


# recursive approach
def binary_search(iter, search):
    if search not in iter:  # let's try and remove these two
        return -1  ########## lines and solve this another way
    midx = len(iter) // 2
    if iter[midx] == search:
        return midx
    elif iter[midx] < search:
        midx += binary_search(iter[midx:], search)
    elif iter[midx] > search:
        midx = binary_search(iter[:midx], search)
    return midx


# procedural approach
def binary_search1(iter, search):
    high = len(iter) - 1
    low = 0

    while low <= high:
        midx = low + ((high - low) // 2)
        if iter[midx] == search:
            return midx
        elif iter[midx] < search:
            low = midx + 1
        else:
            high = midx - 1

    return -1


"""
lst = [1, 2, 3, 4, 5]
search = 2

high = len(lst) - 1
       5        - 1
       4                                        # high = 4
low = 0                                         # low = 0

1. while low <= high:                           # true, 0 <= 4
    mid = 0 + (4 - 0) // 2
          0 + (4 // 2)
          0 + 2
          2                                     # mid = 2
   if lst[mid] == search:                       # lst[2] = 3, != 2, false
   elif lst[mid] < search:                      # lst[2] = 3, !< 2, false
   else:
       high = mid - 1
              2   - 1
              1                                 # high = 1
2. while low <= high:                           # true, 0 <= 1
    mid = 0 + (1 - 0) // 2
          0 + (1 // 2)
          0 + 0
          0                                     # mid = 0
    if lst[mid] == search:                      # lst[0] = 1, != 2, false
    if lst[mid] < search:                       # lst[0] = 1,  < 2, true
        low = mid + 1
              0   + 1
              1                                 # low = 1
3. while low <= high:                           # true, 1 <= 1
    mid = 1 + (1 - 1) // 2
          1 + (0 // 2)
          1 + 0
          1                                     # mid = 1
    if lst[mid] == search:                      # lst[1] = 2, == 2, true
        return mid
               1
"""


"""
ind     0  1  2  3  4
iter = [1, 2, 3, 4, 5]
search = 8

mid_idx = 2
iter[mid_idx] = 3 (less than search)
iter[mid_idx:] = [3, 4, 5]

    og ind  2  3  4
    nw ind  0  1  2
    iter = [3, 4, 5]
    search = 8

    mid_idx = 1
    iter[mid_idx] = 4 (less than search)
    iter[mid_idx:] = [4, 5]

        og ind  3  4
        p1 ind  1  2
        nw ind  0  1
        iter = [4, 5]
        search = 8

        mid_idx = 1
        iter[mid_idx] = 5 (less than search)
        iter[mid_idx:] = [5]

            og ind  4
            p1 ind  2
            p2 ind  1
            nw ind  0
            iter = [5]
            search = 8

            mid_idx = 0
            iter[mid_idx] = 5 (less than search)
            iter[mid_idx:] = [5] ### iter == iter[mid_idx:]

                og ind  4
                p1 ind  2
                p2 ind  1
                p3 ind  0
                nw ind  0
                iter = [5]
                search = 8

                mid_idx = 0
                iter[mid_idx] = 5 (less than search)
"""


# All of these examples should print True
businesses = [
    "Apple Store",
    "Bags Galore",
    "Bike Store",
    "Donuts R Us",
    "Eat a Lot",
    "Good Food",
    "Pasta Place",
    "Pizzeria",
    "Tiki Lounge",
    "Zooper",
]
print(binary_search(businesses, "Pizzeria") == 7)
print(binary_search(businesses, "Apple Store") == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]
print(binary_search(names, "Peter") == -1)
print(binary_search(names, "Tyler") == 6)
