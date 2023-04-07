#!/usr/bin/python3

"""
    No module was imported
"""


def say_my_name(first_name, last_name=""):
    """
        return the fullname of a object


        Args:
            first_name (str): the first name of a person
            last_name (str): the last name of a person
        Raises:
            TypeError: when first or last name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif first_name is None or last_name is None:
        return None
    else:
        print(f"My name is {first_name} {last_name}")
