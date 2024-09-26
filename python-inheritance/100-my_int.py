#!/usr/bin/python3
"""Provides the definition of the MyInt class"""


class MyInt(int):
    """
    Defines the MyInt class; behaves as an int with
    with inverse functionality for == and != operators
    """

    def __eq__(self, value):
        """returns False if self == value"""
        if self == value:
            return False
        return True

    def __ne__(self, value):
        """returns False if self != value"""
        if self != value:
            return False
        return True
