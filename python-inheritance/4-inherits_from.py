#!/usr/bin/python3
"""This module provides a definition for the inherits_from() method"""


def inherits_from(obj, a_class):
    """Returns True is obj is a subclass of a_class"""
    if issubclass(type(obj), a_class):
        return True
    return False
