#!/usr/bin/python3


def search_replace(myList, search, replace):
    return [(replace if i == search else i) for i in myList]
