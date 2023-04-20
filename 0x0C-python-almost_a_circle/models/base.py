#!/usr/bin/python3

"""
    No module was imported
"""


class Base:
    """
        This serves as the base class of the
        other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
