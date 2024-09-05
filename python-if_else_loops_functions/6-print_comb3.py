#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        else:
            print("{:02d}".format((i * 10) + j))
