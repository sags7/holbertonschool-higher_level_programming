#!/usr/bin/python3


def divisible_by_2(myList=[]):
    if len(myList) == 0:
        return
    retList = myList.copy()
    for i in range(len(myList)):
        retList[i] = True if myList[i] % 2 == 0 else False
    return retList
