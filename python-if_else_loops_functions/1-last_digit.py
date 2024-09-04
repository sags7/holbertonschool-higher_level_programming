#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
finalStr = ""
if number > 5:
    finalStr = "and is greater than 5"
elif number == 0:
    finalStr = "and is 0"
elif number < 6:
    finalStr = "and is less than 6 and not 0"

lastDigit = ""
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = -(-number % 10)

print("Last digit of {} is {} {}".format(number, lastDigit, finalStr))
