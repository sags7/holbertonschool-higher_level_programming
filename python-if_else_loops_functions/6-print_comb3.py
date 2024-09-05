#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print(89)
        else:
            print("{:02d}, ".format((i * 10) + j), end="")
