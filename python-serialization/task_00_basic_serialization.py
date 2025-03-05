#!/usr/bin/python3
"""
module provides functionality to serialize and deserialize 
a python dictionary through JSON
"""

import json


def serialize_and_save_to_file(data, filename):
    """serializes a python dictionary into JSON"""
    with open(filename, "w", encoding="utf-8") as file:
        serialized_data = json.dumps(data)
        file.write(serialized_data)


def load_and_deserialize(filename):
    """returns a python dictionary, deserialized form a JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
