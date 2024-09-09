#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    aTuple = (tuple_a + (0, 0))[:2]
    bTuple = (tuple_b + (0, 0))[:2]
    return ((aTuple[0] + bTuple[0]), (aTuple[1] + bTuple[1]))
