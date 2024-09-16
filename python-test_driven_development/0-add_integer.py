#!/usr/bin/python3
"""
add_integer adds two integers and returns the result. For example,

>>> add_integer(5, 4)
9

Args:
    a: first param.
    b: second param, defaults to 98
"""


def add_integer(a, b=98):

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
