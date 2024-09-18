#!/usr/bin/python3
"""
This module provides a the class definition for a Square
"""


class Square:
    """
    Class definition for a Square

    Attributes:
        size (int, float): the size of the square
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size

        Args:
            size (int, float): the size of the square, default is 0
        """

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """validates and sets the size of the square"""

        if not isinstance(size, (float, int)):
            raise TypeError("size must be a number")

        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be a positive number")
