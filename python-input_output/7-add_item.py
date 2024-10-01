#!/usr/bin/python3
"""
this script adds all arguments to a Python list
and saves them to a file
"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys
import os

filename = "add_item.json"
arguments = []

if not os.path.exists(filename):
    save_to_json_file(arguments, filename)
else:
    arguments = load_from_json_file(filename)

for arg in range(1, len(sys.argv)):
    arguments.append(sys.argv[arg])

save_to_json_file(arguments, filename)
