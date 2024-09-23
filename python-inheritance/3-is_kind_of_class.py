#!/usr/bin/python3
"""This module provides a definition for the is_kind_of_class() method"""


def is_kind_of_class(obj, a_class):
    """Returns True is obj is an instance or subclass of a_class"""
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    return False
