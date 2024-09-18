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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
