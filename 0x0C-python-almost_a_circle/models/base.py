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
        """
            writes the JSON strin representation of list_objs to a file
        """
        fname = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                content.append(json_dict)

        with open(fname, "w") as jfile:
            json.dump(content, jfile)
