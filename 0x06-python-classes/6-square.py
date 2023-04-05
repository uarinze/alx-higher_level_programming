#!/usr/bin/python3
"""this class defines a square."""


class Square:
    """This class defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """initilises an instance of the square class.
        Args:
            size: the size of the square
            position: position
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """this retreives the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """this sets the position"""
        if not isinstance(value, tuple)
                or any(idx < 0 for idx in value)
                or len(value) is not 2
                or not all(isinstance(ind, int) for ind in value):
            raise TypeError("position must be a tupple\
                    of two positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the area of the square"""
        areaa = self.__size ** 2
        return areaa

    def my_print(self):
        """prints the square if size is greater than 0."""
        if self.__size > 0:
            for a in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(0, (self.__size + self.__position[0])):
                    if j < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        elif self.__size == 0:
            print()
