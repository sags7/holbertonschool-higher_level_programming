#!/usr/bin/python3


def safe_print_list(myList=[], x=0):
    printed = 0
    try:
        for i in range(x):
            print("{} ".format(myList[i]), end="")
            printed += 1
    except IndexError:
        print("Index out of bounds")
    except:
        print("unknown error")
    print()
    return printed
