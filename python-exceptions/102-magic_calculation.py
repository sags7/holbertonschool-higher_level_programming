#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    try:
        for i in range(a, b):
            if i > a:
                raise Exception("Too far")
            else:
                result += (a**b) / i
    except Exception:
        result = b + a
    return result
