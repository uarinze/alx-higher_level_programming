#!/usr/bin/python3
"""A basegeometry class"""


class BaseGeometry:
    """A class that does nothing."""

    def area(self):
        """An area method that is not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Receiving and validating data"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
