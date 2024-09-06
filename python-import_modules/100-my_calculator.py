#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = int(argv[1])
    b = int(argv[3])
    arlen = len(argv) - 1
    op = argv[2]

    if arlen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit()
    if op not in {"+", "-", "*", "/"}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit()
    if op == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif op == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif op == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif op == "/" and b != 0:
        print(f"{a} / {b} = {div(a, b)}")
