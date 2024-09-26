#!/usr/bin/python3
"""Module provides a definition for the BaseGeometry class"""


class BaseGeometry:
    """Definition of the BaseGeometry class"""

    def area(self):
        """returns the area of the Rectangle"""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """makes sure that value is of the correct type and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
