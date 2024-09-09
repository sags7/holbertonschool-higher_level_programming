#!/usr/bin/python3


def no_c(myString):
    return "".join(char for char in myString if char not in "cC")
