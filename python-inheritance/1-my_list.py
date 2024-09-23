#!/usr/bin/python3
""" This module provides a definition of MyList class"""


class MyList(list):
    """defines the MyList class that derives from list"""

    def print_sorted(self):
        """prints the MyList, sorted, ascending"""
        print(sorted(self))
