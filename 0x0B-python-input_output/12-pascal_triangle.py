#!/usr/bin/python3

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
    triangle = []
    for i in range(n):
        level = 11 ** i
        level = str(level)
        values = []
        for j in level:
            values.append(j)
        triangle.append(values)
    return triangle
