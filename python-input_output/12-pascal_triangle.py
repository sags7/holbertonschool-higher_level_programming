#!/usr/bin/python3
"""module provides the method pascal_triangle(n)"""


def pascal_triangle(n):
    """
    returns a list of lists representing pascal's
    triangle with n levels
        pt = __import__("12-pascal_triangle").pascal_triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
