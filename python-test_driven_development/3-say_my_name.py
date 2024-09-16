#!/usr/bin/python3
"""
This module provides a method that prints the phrase
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints the full name input through the parameters
    passed to the function and  has an empty last name as default

    Args:
        first_name (str): the first name
        last_name (str): the optional last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
