"""
A 90-degree rotation of a matrix produces a new matrix in which each side of the
matrix is rotated clockwise by 90 degrees. Given the following matrix:

    1  5  8
    4  7  2
    3  9  6

The rotation of the matrix is:

    3  4  1
    9  7  5
    6  2  8

A 90-degree rotation of a non-square matrix is similar. For example, given the
following matrix:

    3  4  1
    9  7  5

Its 90-degree rotation is:

    9  3
    7  4
    5  1

Write a function that takes an arbitrary MxN matrix, rotates it clockwise by
90-degrees as described above, and returns the result as a new matrix. The
function should not mutate the original matrix.

Inputs: matrix as a list of nested lists
Outputs: matrix as a list of nested lists

Explicit Rules:
- Function should rotate the list 90-degrees clockwise
    - The first row become the last column
    - The last column becomes the last row
    - The last row becomes the first column
    - The first column becomes the first row
- Function should return a new list; not mutate the input
- Function should work for square and non-square matrices, as long as each
  row has the same number of columns

Implicit Rules:
- Input matrix will always have the same number of columns in each row
- Rotating a matrix 4 times returns it to its original state

Data Structure/s:
- list
- int

Algorithm:
- initalize transposed to a list with the same number of empty lists as columns
- loop through each column index of the input matrix (0, 1, 2):
    loop through each row index of the input matrix in reverse order (2, 1, 0):
        append the matrix element at [row][col] to the [col] list in transposed
- return transposed

Notes:
Matrix represented by chained index calls:
    [0][0]  [0][1]  [0][2]
    [1][0]  [1][1]  [1][2]
    [2][0]  [2][1]  [2][2]

Rotation:
    [2][0]  [1][0]  [0][0]      loop through col idx 0 of row idxes 2, 1, 0
    [2][1]  [1][1]  [0][1]      loop through col idx 1 of row idxes 2, 1, 0
    [2][2]  [1][2]  [0][2]      loop through col idx 2 of row idxes 2, 1, 0
"""


def transpose(mtx):
    return [[mtx[row][col] for row in range(len(mtx))] for col in range(len(mtx[0]))]


def rotate90_1(mtx):
    transposed = [[] for _ in range(len(mtx[0]))]
    for col in range(len(mtx[0])):
        for row in reversed(range(len(mtx))):
            transposed[col].append(mtx[row][col])
    return transposed


def rotate90_2(mtx):
    return [
        [mtx[row][col] for row in reversed(range(len(mtx)))]
        for col in range(len(mtx[0]))
    ]


def rotate90_3(mtx):  # transposes mtx and then reverses elem order in each row
    return [[*reversed(row)] for row in transpose(mtx)]


def rotate90(mtx):  # reverses order of rows, and then zips its contents
    return [list(row) for row in zip(*reversed(mtx))]


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
