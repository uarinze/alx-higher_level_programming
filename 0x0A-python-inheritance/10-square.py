#!/usr/bin/python3
"""A class that inherits from another."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialisation for the objects of Square class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
