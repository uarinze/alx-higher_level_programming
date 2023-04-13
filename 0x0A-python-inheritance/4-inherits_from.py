#!/usr/bin/python3


def inherits_from(obj, a_class):
    """This function returns true if the object
    is an instance of a claass that inherited
    (direclty or indirectly) from the specified class;
    otherwise false.
    """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    else:
        return False
