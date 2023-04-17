#!/usr/bin/python3

"""
    help convert datatype to json
"""

import json


def from_json_string(my_obj):
    """
        converts text to json

        Args:
            my_obj(json): convert string to json
    """

    json_repr = json.loads(my_obj)
    return json_repr
