#!/usr/bin/python3
"""provides the definition for from_json_string()"""

import json


def from_json_string(my_str):
    """returns a python object represented by a JSON string"""
    return json.loads(my_str)
