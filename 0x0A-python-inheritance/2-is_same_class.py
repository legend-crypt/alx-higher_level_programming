#!/usr/bin/python3

"""
    No module was importd
"""


def is_same_class(obj, a_class):
    """
        Check if an object is an instance of a class
    """

    x = type(obj)
    if x == a_class:
        return True
    return False
