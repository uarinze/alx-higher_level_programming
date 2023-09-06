#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """Adds two integers a and b.
    If a and b are not integers or floats, raises an exception.
    If a or b is float, they are casted forst to integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
