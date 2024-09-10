#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return
    top = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        top = key if a_dictionary[key] > a_dictionary[top] else top
    return top
