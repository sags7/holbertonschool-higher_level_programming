#!/usr/bin/python3
"""Module provides then definition of Animal, Dog and Cat classes"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """The abstract definition of the Animal class"""

    @abstractmethod
    def sound(self):
        """Abstract definition of sound"""
        pass


class Dog(Animal):
    """The concrete implementation of the Dog class"""

    def sound(self):
        """concrete definition of sound() for the Dog class"""
        return "Bark"


class Cat(Animal):
    """The concrete implementation of the Cat class"""

    def sound(self):
        """concrete definition of sound() for the Cat class"""
        return "Meow"
