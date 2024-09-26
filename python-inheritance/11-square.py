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
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Returns the string representation of Square"""
        return "[Square] {}/{}".format(self.__width, self.__height)

    def area(self):
        """returns the area of the Square"""
        return self.__size**2
