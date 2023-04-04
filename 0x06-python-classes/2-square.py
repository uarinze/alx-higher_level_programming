#!/usr/bin/python3
"""This is a class that defines a square"""


class Square:
    """This is a sqaure"""
    def __init__(self, size=0):
        """The init method that initialises the fields for each instance.

        Args:
            size: this is an optional int field.
        """
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
