#!/usr/bin/python3
"""this class defines a square."""


class Square:
    """This class defines a square."""
    def __init__(self, size=0):
        """initilises an instance of the square class.
        Args:
            size: the size o the square
        """
        self.__size = size
    @property
    def size(self):
        """This is a property getter thatretrieves the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the value of size."""
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of the square"""
        areaa = self.__size * self.__size
        return areaa

    def my_print(self):
        """prints the square if size is greater than 0."""
        if self.__size > 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        elif self.__size == 0:
            print()
   
