#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """This function returns true if the object
    is an instance of, or if the object is an
    instance of a class that inherited from the sspecified class
    otherwise returnfalse.
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
