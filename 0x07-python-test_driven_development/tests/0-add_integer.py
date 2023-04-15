#!/usr/bin/python3
"""
    No module was imported
"""


def add_integer(a, b=98):

    """
        This function adds to two int or float numbers

        Args:
            a (int, float): first arguement to add
            b (int, float): second arguement to add

        Return:
            int: the sum of the operation
        Raises:
            TypeError: if a or b is not int
    """

    chk_a = isinstance(a, (int, float))
    chk_b = isinstance(b, (int, float))

    if chk_a and chk_b:
        return a + b
    elif chk_a is True and chk_b is False:
        raise TypeError("b must be an integer")
    elif chk_a is False and chk_b is True:
        raise TypeError("a must be an integer")
