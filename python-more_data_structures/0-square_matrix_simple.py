#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    pows = []
    for element in matrix:
        pows += [list(map(lambda x: x**2, element))]
    return pows
