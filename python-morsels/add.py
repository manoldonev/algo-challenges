"""I'd like you to write a function that accepts two lists-of-lists of numbers
and returns one list-of-lists with each of the corresponding numbers in the
two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]"""


def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    matrix_shapes = {
        tuple(len(row) for row in matrix)
        for matrix in matrices
    }

    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size.")

    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
