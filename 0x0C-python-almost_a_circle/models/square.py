#!/usr/bin/python3

"""
    Import Rectangle class
"""
import base.Rectangle


class Square(Rectangle):
    """
        This class implement a square
        it inherit from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width, height, id=id, x=0, y=0)
        self.size = width

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.name,
                self.__x,
                self.__y,
                self.size)
