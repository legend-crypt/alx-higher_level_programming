#!/usr/bin/python3

"""
    json package is imported to serve as a helping
    function
"""
import json


class Base:
    """
        This serves as the base class of the
        other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return the json representation of
            class atrributes

            Args:
                list_dictionaries(dict): the dictionary to be converted json
        """
        if list_dictionaries is None:
            return "[]"
        json_repr = json.dumps(list_dictionaries)
        return json_repr

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(new_list))
