#!/usr/bin/python3


def safe_print_list_integers(myList=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print(f"{myList[i]:d}", end="")
            printed += 1
        except (IndexError, TypeError, ValueError):
            pass
    print()
    return printed
