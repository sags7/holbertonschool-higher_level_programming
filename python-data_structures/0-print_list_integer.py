#!/usr/bin/python3


def print_list_integer(list=[]):
    print("{:d}\n".format(list[i] for i in range(0, len(list) - 1)), end="")
