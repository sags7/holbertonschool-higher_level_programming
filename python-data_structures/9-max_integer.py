#!/usr/bin/python3


def max_integer(myList=[]):
    if len(myList) == 0:
        return None
    maxValue = myList[0]
    for item in myList:
        if item > maxValue:
            maxValue = item
    return maxValue
