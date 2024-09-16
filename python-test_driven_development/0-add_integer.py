#!/usr/bin/python3
"""
This module provides a function called add_integer that adds two integers.
"""


def add_integer(a, b=98):
    """
    add_integer adds two integers and returns the result. For example,

    >>> add_integer(5, 4)
    9

    Args:
       a (int, float): first param.
       b (int, float): second param, defaults to 98
    Returns:
        The sum of a and b as an int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if abs(a) > 1e308 or abs(b) > 1e308:
        raise OverflowError("cannot convert float infinity to integer")

    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
