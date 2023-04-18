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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            convert the instance variables to
            dictionary
        """
        serialized_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return serialized_dict
