#!/usr/bin/python3
"""module provides the write_file() method definition"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename, "w", "utf-8") as f:
        f.write(text)
