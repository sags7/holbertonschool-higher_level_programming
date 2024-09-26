#!/usr/bin/python3
"""Provides the definition of the add_attribute() function"""


def add_attribute(ob, name, value):
    """
    Checks if ob allows the dynamic creation of attributes
    and adds it with the given value, or raises an error

        Args:
            ob (object): the object to add an attribute to
            name (str): the name of the attribute
            value: the value of the attribute
    """

    if hasattr(ob, __dict__):
        ob.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
