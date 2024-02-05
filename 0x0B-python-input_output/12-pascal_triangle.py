#!/usr/bin/python3

"""
    no module was imported
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing
        the Pascal's triangle of n

        Args:
            n(int): The pascal coefficient
        Returns:
            triangle(list): a list of list reprensenting the
                pascal triangle
    """
    triangle = [[1]]
    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1])+ 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle
