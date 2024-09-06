#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def my_calc(a, b):
    arlen = len(sys.argv) - 1
    op = sys.argv[2]

    if arlen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit()
    if op not in {"+", "-", "*", "/"}:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit()
    if op == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif op == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif op == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif op == "/" and b != 0:
        print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    my_calc(int(sys.argv[1]), int(sys.argv[3]))
