#!/usr/bin/python3
"""Module provides a definition for the Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines the Square class derived from Rectangle

    Args:
        size (int): the size of the sides of the square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
