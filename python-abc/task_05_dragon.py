#!/usr/bin/python3
"""defines SwimMixin, FlyMixin, and Dragon classes"""


class SwimMixin:
    """provides swimming functionality"""

    def swim(self):
        """prints a message to to stdout"""
        print("The creature swims!")


class FlyMixin:
    """provides flying functionality"""

    def fly(self):
        """prints a message to to stdout"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """defines the Dragon class"""

    def roar(self):
        """prints a message to stdout"""
        print("The dragon roars!")
