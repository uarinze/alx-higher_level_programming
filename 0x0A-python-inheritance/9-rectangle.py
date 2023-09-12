#!/usr/bin/python3
"""A class that inherits from another."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialisation for the bjects of Rectangle class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Formats the output"""
        ret = "[" + str(self.__class__.__name__) + "] "
        ret += str(self.__width) + "/" + str(self.__height)
        return ret

    def area(self):
        """Returns the area of the object"""
        return self.__width * self.__height
