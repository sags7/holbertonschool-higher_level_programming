#!/usr/bin/python3
"""Module provide the definition of the VerboseList class"""


from typing import Iterable, SupportsIndex


class VerboseList(list):
    """
    VerboseList prints notifications every time an
    item is added or removed
    """

    def append(self, object):
        """adds object to the end of the list"""
        super().append(object)
        print("Added [{}] to the list".format(object))

    def extend(self, iterable):
        """extends a list by via an iterable"""
        super().extend(iterable)
        print("Extended the list with [{}] items".format(len(iterable)))

    def remove(self, item):
        """removes an item from the list"""
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=None):
        """
        Removes item at index or the last item if no index is passed.
        """
        if index is None:
            popped = super().pop()
            print("Popped [{}] from the list".format(popped))
            return popped
        else:
            popped = super().pop(index)
            print("Popped [{}] from the list".format(super().pop(index)))
            return popped
