#!/usr/bin/python3
"""A class that inherits from another."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialisation for the bjects of Rectangle class"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
