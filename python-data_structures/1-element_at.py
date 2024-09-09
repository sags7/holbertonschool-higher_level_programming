#!/usr/bin/python3


def element_at(myList, index):
    if index < 0 or index >= len(myList):
        return None
    return myList[index]
