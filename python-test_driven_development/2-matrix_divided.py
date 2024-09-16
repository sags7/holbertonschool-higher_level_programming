#!/usr/bin/python3
"""
This module provides a function that returns a new matrix with each
element being the division of an element from matrix divided by div
"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides each element of matrix by div and
    returns a new matrix with the result

    >>> matrix_divided([[10,6], [6,10]], 2)
    [[5, 3], [3, 5]]

    Args:
        matrix (list of lists): the matrix to divide
        div (int, float): the divisor
    Returns:
        a new matrix with the result of the division
        of each element of matrix by div
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(err)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err)
    if div == float("inf") or div == -float("inf"):
        return [[0.0 for element in row] for row in matrix]

    retVal = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err)

    retVal = [[round((element / div), 2) for element in row] for row in matrix]

    if not all(isinstance(e, (int, float)) for e in row for row in retVal):
        TypeError(err)

    return retVal
