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
    for character in text:
        if character in ".?:":
            print(f"{character}\n")
        elif character not in " ":
            print(character, end="")
