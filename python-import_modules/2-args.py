#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arlen = len(sys.argv) - 1
    if arlen == 0:
        print("0 arguments.")
    elif arlen == 1:
        print(f"1 argument:\n1: {sys.argv[1]}")
    else:
        print(f"{arlen} arguments:")
        for i in range(1, arlen + 1):
            print(f"{i}: {sys.argv[i]}")
