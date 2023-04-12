#!/usr/bin/python3

"""
    No module was imported
"""


class BaseGeometry:
    """
        The base geometry class raise an with the
        message
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if isinstance(value, int) and value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        creates a rectangle by inheriting from the
        BaseGeometry class
    """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
