#!/usr/bin/python3
"""provides the definition for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line that contains
    a specific string
    """

    with open(filename, "r", encoding="utf-8") as file:
        original_text = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in original_text:
            file.write(line)
            if search_string in line:
                file.write(new_string)
