#!/usr/bin/python3
"""
Module provides definitions for Shape, Circle and Rectangle
classes, as well as the shape_info() method
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """The abstract definition of the Shape class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete definition of the Circle class"""

    def __init__(self, radius):
        """initialization of Circle"""
        self.__radius = radius

    def area(self):
        """returns the area of a circle depending on radius"""
        return abs(3.141592653589793 * self.__radius * self.__radius)

    def perimeter(self):
        """returns the perimeter of a circle based on radius"""
        return abs(2 * 3.141592653589793 * self.__radius)


class Rectangle(Shape):
    """Concrete definition of the Rectangle class"""

    def __init__(self, width, height):
        """initialization of Rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of a Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of a Rectangle"""
        return (self.__width + self.__height) * 2


def shape_info(object):
    """prints the area and perimeter relying on duck typing"""
    print("{:.1f}".format(object.area()))
    print("{:.1f}".format(object.perimeter()))
