#!/usr/bin/python3


def print_list_integer(MyList=[]):
    print("".join("{:d}\n".format(item) for item in MyList), end="")
