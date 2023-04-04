#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This initialises instances of the square
        Args:
            size: this is an optional int field."""
        if (isinstance(size, int) is not True):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """this method returns the area of the square.
        Args: None
        Returns: area of square."""
        self.areaa = self.__size * self.__size
        return self.areaa
