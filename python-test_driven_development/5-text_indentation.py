#!/usr/bin/python3
"""
this module provides a function that prints a text with
2 new lines after each of these characters '.?:'
"""


def text_indentation(text):
    """
    text_indentation prints a text to the console, adding
    2 new lines after each of these characters '.?:'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skipChar = False
    for character in text:
        if character in ".?:":
            print(f"{character}\n")
            skipChar = True
        elif skipChar and character in "    ":
            continue
        else:
            skipChar = False
            print(character, end="")
