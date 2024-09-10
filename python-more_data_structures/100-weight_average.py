#!/usr/bin/python3


def weight_average(myList=()):
    if len(myList) == 0:
        return 0
    dividend = sum(value * weight for value, weight in myList)
    divisor = sum(weight for value, weight in myList)
    return (dividend / divisor) if divisor != 0 else 0
