#!/usr/bin/python3

"""
    No module was imported
"""


class Student:
    """
        A student class the defines a student by his
        first name, lastname and age
        and the instance in form of a dictionary
        for json serialization
    """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
            convert the instance variables to
            dictionary if the arguement provided is list

            Args:
                attrs(list, string): the named value we returning
        """
        if attrs is None:
            return self.__dict__
        else:
            if isinstance(attrs, list):
                return {
                        attr: getattr(self, attr) for attr in attrs
                        if hasattr(self, attr) and isinstance(attr, str)
                        }
