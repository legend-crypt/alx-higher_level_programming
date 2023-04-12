#!/usr/bin/python3
"""
    No module was imported
"""


def inherits_from(obj, a_class):
    """
        returns true if obj is a subclass of a class
    """
    if issubclass(obj.__class__, a_class):
        if obj.__class__ is not a_class:
            return True
    else:
        return False
