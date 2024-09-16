#!/usr/bin/python3


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

    return int(a) + int(b)
