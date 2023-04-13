#!/usr/bin/python3


    """Function that returns true if the
    object is exactly an instance of the specified class;
    otherwise false.
    """

def is_same_class(obj, a_class):
    """Function that returns true if the
    object is exactly an instance of the specified class;
    otherwise false.

    Args:
        obj: an object
        a_class: a class
    Returns:
        True if object is exactly an instance of a_class
        False otherwise
    """
    if (type(obj) == a_class):
        return True
    else:
        return False
