#!/usr/bin/python3
"""
this module serves as an example of
how to de/serialize custom classes
"""

import pickle
import os


class CustomObject:
    """example of a custom object to serialize"""

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displays the attributes of the custom obj to stdout"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """pickles the CustomObject"""
        with open(filename, "wb") as file:
            try:
                pickle.dump(self, file)
            except pickle.PicklingError:
                print("unpickable object encountered by pickle")
                return None

    @classmethod
    def deserialize(cls, filename):
        """depickles the serialized custom obj"""
        if not os.path.exists(filename):
            print("file to unpickle does not exist")
            return None
        with open(filename, "rb") as file:
            try:
                return pickle.load(file)
            except (pickle.UnpicklingError, EOFError, OSError) as err:
                print(f"error trying to unpickle the object: {err}")
                return None
