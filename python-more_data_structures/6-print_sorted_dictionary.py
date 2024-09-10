#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    print(
        "".join(
            "{}: {}\n".format(i, a_dictionary[i])
            for i in sorted(a_dictionary.keys())
        ),
        end="",
    )
