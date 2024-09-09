#!/usr/bin/python3


def replace_in_list(myList, index, element):
    if index < 0 or index >= len(myList):
        return myList
    myList[index] = element
    return myList
