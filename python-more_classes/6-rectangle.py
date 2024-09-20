#!/usr/bin/python3
"""
this module provides the definition of the Rectangle class
"""


class Rectangle:
    """Defines the Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the instance with optional width and height"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """Returns the Rectangle as a string"""
        if self.width == 0 or self.height == 0:
            return ""

        result = ""
        for i in range(self.height):
            result += "#" * self.width
            if i < self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """Returns the official representation of the Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Called right before deleting an instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the Rectangle instance"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
