#!/usr/bin/python3
"""
print_square prints square of the given size to the console
"""


def print_square(size):
    """
    print_square prints a size sized square to the console

    Args:
        size (int): the size of the square in #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        print("".join("#" for x in range(size)))
    print()
