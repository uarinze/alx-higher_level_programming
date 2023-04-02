#!/usr/bin/python3


def safe_print_division(a, b):
    '''
    This function divides 2 integers and prints the result
    Args:
        a: first integer
        b: second integer
    Returns:
        the result of the division or None otherwise
    '''
    try:
        res = a / b
    except (ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return(res)
