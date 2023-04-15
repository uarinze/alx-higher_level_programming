#!/usr/bin/python3
"""A class that does nothing but raise an exception"""


class BaseGeometry(object):
    """A class that does nothing."""
    def area(self):
        raise Exception("area() is not implemented")
