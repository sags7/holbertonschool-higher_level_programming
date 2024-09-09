#!/usr/bin/python3


def print_list_integer(myList=[]):
    print("".join("{:d}\n".format(item) for item in myList), end="")
