#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function divides the elements of a matrix"""
    if type(matrix) is not list or matrix == [] \
            or not all(isinstance(row, list) for row in matrix) \
            or not all((isinstance(num, int) or isinstance(num, float))
                    for num in [item for row in matrix for item in row]):
        raise TypeError("matrix must be a matrix \
        (list of list) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
