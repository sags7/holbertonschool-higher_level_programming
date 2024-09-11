#!/usr/bin/python3


def safe_print_list_integers(myList=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(myList[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            pass
    print()
    return printed
