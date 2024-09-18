#!/usr/bin/python3
"""
This module provides a the class definition for a Square
"""


class Square:
    """
    Class definition for a Square

    Attributes:
        size (int, float): the size of the square
        position (int, int): the position of the square in space
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position

        Args:
            size (int, float): the size of the square, default is 0
            position (int, int): the position of the square in space
        """

        self.size = size
        self.position = position

    def __str__(self):
        """Returns the square as a string"""
        if self.size == 0:
            return ""

        result = "\n" * self.position[1]
        for i in range(self.size):
            result += " " * self.position[0] + "#" * self.size
            if i < self.size - 1:
                result += "\n"
        return result

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """validates and sets the size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Returns a tuple with the position of the square in 2D space"""
        return self.__position

    @position.setter
    def position(self, position):
        if (
            not all(isinstance(elem, int) for elem in position)
            or len(position) != 2
            or not all(elem >= 0 for elem in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """returns the area of the square"""
        return self.size**2

    def my_print(self):
        """Prints the square to stdout"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
