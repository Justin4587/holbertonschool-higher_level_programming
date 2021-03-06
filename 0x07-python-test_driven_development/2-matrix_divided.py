#!/usr/bin/python3
""" how many times can this int enter this int """


def matrix_divided(matrix, div):
    """ int penetrators """


    if type(div) == float("inf"):
        raise OverflowError("cannot convert float infinity to integer")
    if type(div) == float("Nan"):
        raise ValueError("cannot convert float NaN to integer")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (row of rows) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (row of rows) of integers/floats")

    items = len(matrix[0])
    for i in matrix:
        if len(i) != items:
            raise TypeError("Each row of the matrix must have the same size")


    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    return [[float("{:.2f}".format(num/div)) for num in row] for row in matrix]
