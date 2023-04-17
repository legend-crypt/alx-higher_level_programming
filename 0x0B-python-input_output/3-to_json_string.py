#!/usr/bin/python3

import json

"""
    access a text as a json repr
"""


def to_json_string(my_obj):
    """
        converts text to json

        Args:
            my_obj(json): convert string to json
    """

    json_repr = json.dumps(my_obj)
    return json_repr
