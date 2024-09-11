#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except TypeError as e:
        print("Exception: {e}", file=sys.stderr)
