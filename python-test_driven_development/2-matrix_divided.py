#!/usr/bin/python3
"""
This is the divided matrix module.
This module supplies one function, matrix_divided()
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Given two arguments a matrix and div
    (is a ramdon integer)
    Return a matrix with values divided for the div
    """
    if type(matrix) is not list:
        raise (TypeError("matrix must be a matrix \
(list of lists) of integers/floats"))

    for idx in matrix:
        for number in idx:
            if not (isinstance(number, (int, float))):
                raise (
                    TypeError("matrix must be a matrix \
(list of lists) of integers/floats"))

    if not all(map(lambda rows: len(matrix[0]) == len(rows), matrix)):
        raise (TypeError("Each row of the matrix must have the same size"))

    if not isinstance(div, (int, float)):
        raise (TypeError("div must be a number"))

    if div == 0:
        raise (ZeroDivisionError("division by zero"))

    return [[round(number / div, 2)for number in div_list]
            for div_list in matrix]
