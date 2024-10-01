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

    def to_json(self):
        """returns all the attributes that can be serialized as JSON"""
        return self.__dict__
