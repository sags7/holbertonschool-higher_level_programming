#!/usr/bin/python3
print("".join("{:02d}, ".format(n) for n in range(0, 100) if n != 99), end="")
print("{}".format(99))
