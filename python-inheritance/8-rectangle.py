#!/usr/bin/python3
"""Module provides the definition of the Rectangle and BaseGeometry classes"""


class Rectangle(BaseGeometry):
    """Defines a Rectangle class derived from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
