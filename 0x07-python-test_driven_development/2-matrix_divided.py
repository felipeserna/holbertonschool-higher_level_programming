#!/usr/bin/python3
"""
Divides all elements of a matrix
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Args: matrix: list of lists of integers or floats.
    div: integer or float different from 0
    """
    new_matrix = matrix.copy()
    same_size = "Each row of the matrix must have the same size"
    int_float = "matrix must be a matrix (list of lists) of integers/floats"

    if isinstance(matrix, list):
        for row in new_matrix:
            if isinstance(row, list):
                if len(new_matrix[0]) == len(row):
                    for col in row:
                        if type(col) in [int, float]:
                            pass
                        else:
                            raise TypeError(int_float)
                else:
                    raise TypeError(same_size)
            else:
                raise TypeError(int_float)
    else:
        raise TypeError(int_float)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i/div,2) for i in row] for row in new_matrix[:]]
