#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function divides the elements of a matrix
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
    A new matrix representing the result of the division.
    """
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
