#!/usr/bin/python3


def print_reversed_list_integer(myList=[]):
    print("".join("{:d}\n".format(item) for item in reversed(myList)), end="")
