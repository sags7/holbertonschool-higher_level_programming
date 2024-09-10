#!/usr/bin/python3


def roman_to_int(roman):
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    val = 0
    if not roman or not isinstance(roman, str):
        return 0

    for i in range(len(roman) - 1):
        if roman[i] not in nums:
            return 0
        if nums[roman[i]] < nums[roman[i + 1]]:
            val -= nums[roman[i]]
        else:
            val += nums[roman[i]]

    if roman[-1] not in nums:
        return 0
    val += nums[roman[-1]]

    return val
