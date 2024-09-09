#!/usr/bin/python3


def new_in_list(myList, index, elem):
    if index < 0 or index >= len(myList):
        return myList
    newList = myList.copy()
    newList[index] = elem
    return newList
