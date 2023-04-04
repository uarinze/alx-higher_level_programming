#!/usr/bin/python3
"""This is a class that defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """initialises size to 0 for every instance of the square class.."""
        self.size = size

    @property
    def size(self):
        """This is a property getter that retrieves tha value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is a property setter that sets tha value of size."""
        if (isinstance(value, int)) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This is a public method that returns the area of the square.
        Args: None
        Return: area."""
        areaa = self.__size * self.__size
        return areaa

