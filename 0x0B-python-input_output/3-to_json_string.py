#!/usr/bin/python3

"""
    help convert datatype to json
"""

import json


def to_json_string(my_obj):
    """
        converts text to json

        Args:
            my_obj(json): convert string to json
    """

    json_repr = json.dumps(my_obj)
    return json_repr
