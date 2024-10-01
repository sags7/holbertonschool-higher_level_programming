#!/usr/bin/python3
"""module provides the read_file() method definition"""


def read_file(filename=""):
    """read_file(filename) prints the the content of filename to stdout"""

    with open(filename, "r", encoding="utf-8") as f:
        f.read()
