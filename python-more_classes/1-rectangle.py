#!/usr/bin/python3
"""
this module provides the definition of the Rectangle class
"""


class Rectangle:
    """Defines the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the instance with optional width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks the value and sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks the value and sets the height of the Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
