#!/usr/bin/python3
"""module provides a definition for to_json_string()"""

import json


def to_json_string(my_obj):
    """returns the JSON (str) representation of an object"""
    return json.dumps(my_obj)
