"""
In the previous exercise, you wrote a function that transposed a 3x3 matrix
represented by a list of lists.

Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any
matrix can be transposed simply by switching columns with rows.

Modify your transpose function from the previous exercise so that it works with
any MxN matrix with at least one row and one column.

Inputs: matrix as nested lists inside a list
Outputs: matrix as nested lists inside a list

Explicit Rules:
- this function should be able to transpose matrices that are not square,
  i.e. those that don't have the same number of rows as they do columns

Implicit Rules:
- return a new list; don't mutate the input
- every row of the input matrix will have the same number of columns
- if the input matrix is M x N, the output will be an N x M matrix
- if the input matrix only has 1 row with 1 element, the output matrix will
  be the same as the input matrix
- if the input matrix only has 1 row of N elements, the output matrix will
  have N rows of 1 element each. The zip method will not work in this case.

Data Structure/s:
- list
- int

Algorithm:
similar to the explicit nested for loop algorithm?
"""


def transpose1(mtx):
    transposed = [[] for _ in mtx[0]]
    for row in mtx:
        for col in range(len(mtx[row])):
            transposed[col].append(row[col])
    return transposed


def transpose(mtx):
    return [[row[col] for row in mtx] for col in range(len(mtx[0]))]


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)
