#!/usr/bin/python3


def complex_delete(aDictionary, value):
    keysToDelete = [key for key, val in aDictionary.items() if val == value]
    for key in keysToDelete:
        del aDictionary[key]

    return aDictionary
