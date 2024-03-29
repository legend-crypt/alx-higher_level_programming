#!/usr/bin/python3

"""
    help convert json
"""
import json


def save_to_json_file(my_obj, filename):
    """
        write a string as json to a file

        Args:
            my_obj(str): the string to be converted to json
            filename: the file we are writing into
    """

    with open(filename, mode='w', encoding="utf-8") as new_file:
        json.dump(my_obj, new_file)
