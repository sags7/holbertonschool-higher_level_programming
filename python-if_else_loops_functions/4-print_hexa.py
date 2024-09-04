#!/usr/bin/python3
print("".join("{} = {}\n".format(number, hex(number))
              for number in range(0, 99)), end="")
