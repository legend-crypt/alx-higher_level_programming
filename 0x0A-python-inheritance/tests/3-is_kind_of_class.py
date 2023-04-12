#!/usr/bin/python3

"""
    No module was imported
"""


def is_kind_of_class(obj, a_class):
    """
        check if an object is an instance of a class or subclass
    """

    if isinstance(obj, a_class):
        return True
    elif issubclass(obj, a_class):
        return True
    else:
        return False
