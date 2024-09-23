#!/usr/bin/python3
"""This module provides the is_same_class() method"""


def is_same_class(obj, a_class):
    """Returns true if obj is of the same class as a_class"""
    return type(obj) is a_class
