#!/usr/bin/python3

"""
    No module was imported
"""


def matrix_divided(matrix, div):
    """
        This function divides each element in a matrix by div
        and return a new list

        Args:
            matrix (list): must be a list of lists
            div (int, float): divides the the matrix
        Raises:
            TypeError: if maxtrix is not a list or element are
                are not int or float
            ZeroDivisionError: if div is 0
    """
    new_matrix = []

    try:
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for i in range(len(matrix)):
            row = []
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the \
same size")
            if not isinstance(matrix[i], list):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            for a in range(len(matrix[i])):
                if not isinstance(matrix[i][a], (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
                elif not isinstance(div, (int, float)):
                    raise TypeError("div must be a number")
                else:
                    row.append(round(matrix[i][a] / div, 2))
            new_matrix.append(row)
        return new_matrix
    except ZeroDivisionError:
        print("division by 0")
