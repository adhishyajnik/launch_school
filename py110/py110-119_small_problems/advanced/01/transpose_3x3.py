"""
In Python, a matrix can be written as a list of lists (also called a nested list
or a 2-dimensional list). To access an element, we use matrix[row][col].
To return an entire row, we use matrix[row].

The transpose of a 3x3 matrix is the matrix that results from exchanging the
rows and columns of the original matrix.

Given the following matrix:
    matrix = [
        [1, 5, 8],
        [4, 7, 2],
        [3, 9, 6],
    ]

The transposition of the matrix would be:

    matrix = [
        [1, 4, 3],
        [5, 7, 9],
        [8, 2, 6],
    ]

Write a function that takes a list of lists that represents a 3x3 matrix and
returns the transpose of the matrix. You should implement the function on your
own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a new
matrix and leave the input matrix list unchanged.

Inputs: list with 3 nested lists, each containing 3 elements
Outputs: list with 3 nested lists, each containing 3 elements

Explicit Rules:
- a matrix transposition swaps columns for rows, starting from the upper-most
  element of the left-most column
- function must return a new list, not mutate the input
- input will be a 3x3 matrix

Implicit Rules:
- in the transposition, the first row contains all the elements at index 0 of
  the nested lists, the second row contains index 1 elements, and the third row
  contains index 2 elements
- this will require a loop within a loop, or a nested comprehension

Data Structure/s:
- list
- nested list

Algorithm:
- initialize a list with three empty lists inside it, to transposed
- loop through each r in a range from 0 to 3:
    - loop through each c in a range from 0 to 3 (i.e. 0, 1, 2)
        - append the element at row r, column c to transposed c
- return transposed
"""


def transpose1(mtx):
    transposed = [[] for _ in mtx[0]]
    for row in mtx:
        for col in range(len(mtx[row])):
            transposed[col].append(row[col])
    return transposed


def transpose(mtx):
    return [[row[col] for row in mtx] for col in range(len(mtx[0]))]


def transpose2(mtx):
    return [list(row) for row in zip(*mtx)]
    # this works because zipping will automatically put together the index 0
    # elements, put together the index 1 elements, and put together the
    # index 2 elements.


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]


new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]])  # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])  # True
