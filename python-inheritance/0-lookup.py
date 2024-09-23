#!/usr/bin/python3
"""This modules provides a definition of the lookup() method"""


def lookup(myobject):
    """returns a list with all the attributes of the passed object
    Args:
        myobject (object): the object of which to return a list of attributes
    """
    return dir(myobject)
