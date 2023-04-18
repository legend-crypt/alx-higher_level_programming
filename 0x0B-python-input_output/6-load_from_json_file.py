#!/usr/bin/python3

"""
    helper for working in json
"""
import json


def load_from_json_file(filename):
    """
        Create a new file a new json file

        Args:
            filename: a new file
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        data = json.load(file)
    return data
