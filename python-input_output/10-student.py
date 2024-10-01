#!/usr/bin/python3
"""
provides a definition for the Student class
"""


class Student:
    """definition of the Student class"""

    def __init__(self, first_name, last_name, age):
        """initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns all the attrs that can be serialized as JSON"""
        if attrs == None:
            return self.__dict__
        else:
            retVal = {}
            if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
                for atr in attrs:
                    if atr in self.__dict__:
                        retVal[atr] = self.__dict__[atr]
            return retVal
