#!/usr/bin/python3
"""A basegeometry class"""


class BaseGeometry(object):
    """A class that does nothing."""

    def area(self):
        """An area method that is not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Receiving and validating data"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
