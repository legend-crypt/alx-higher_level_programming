#!/usr/bin/python3

"""
    No module was imported
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This class implement a square
        it inherit from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id,
                self.x,
                self.y,
                self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
            This function updates the value
            of the square attribute

            Args:
                id (int): The id of the instance
                size (int): the size of the square
                x (int): the x-axis position of the square
                y (int): the y-axis position of the square
        """
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        if not args:
            if "id" in kwargs and kwargs["id"] is not None:
                self.id = kwargs["id"]
            if "size" in kwargs and kwargs["size"] is not None:
                self.size = kwargs["size"]
            if "x" in kwargs and kwargs["x"] is not None:
                self.x = kwargs["x"]
            if "y" in kwargs and kwargs["y"] is not None:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            Convert clas attribute to dictionary and return it
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
