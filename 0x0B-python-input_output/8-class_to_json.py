#!/usr/bin/python3

"""
    No module was imported
"""


def class_to_json(obj):
    """
        Return the instance of a class as a
        dictionary
        Args:
            obj(dict, list, int, tuple): the class instance data
    """

    serialized_dict = obj.__dict__
    return serialized_dict
