#!/usr/bin/python3
"""Provides a definition for CountedIterator class"""


class CountedIterator:
    """extends the functionality provided by the iter"""

    def __init__(self, iterable):
        """initializes the CountedIterator"""
        self.__iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """returns the number of tracked iterables"""
        return self.__count

    def __next__(self):
        """increments the count each time its called"""
        try:
            item = next(self.__iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """returns itself as an iterator"""
        return self
