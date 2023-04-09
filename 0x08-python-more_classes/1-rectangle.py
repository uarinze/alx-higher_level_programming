#!/usr/bin/python3
"""Module defines a rectangle class"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialises the instance fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the value of width"""
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the value of height"""
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
