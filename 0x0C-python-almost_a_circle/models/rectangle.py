#!/usr/bin/python3

"""
    imported base class which serves as the
    base class for rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
        This class defines a rectangle and
        inherit from base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__,
                self.id,
                self.__x, self.__y,
                self.__width, self.__height
                )

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
            takes the height and widht of the class
            calculate the area the of the rectangle
            and return it
        """
        return self.__width * self.__height

    def display(self):
        """
            takes the height and width attribute of the class
            and print the the rectangle using #
        """
        # if self.__width or self.__height == 0:
        # print()
        for y_axis in range(self.__y):
            print()
        for i in range(self.__height):
            for x_axis in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
            assign the the attribute based on the args position

            Args:
                id (int): The id attribute
                width (int): the width attribute
                height (int): the height attribute
                x (int): the x attribute
                y (int): the y attribute
        """
        if args:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

        if not args:
            if "id" in kwargs and kwargs["id"] is not None:
                self.id = kwargs["id"]
            if "height" in kwargs and kwargs["height"] is not None:
                self.height = kwargs["height"]
            if "width" in kwargs and kwargs["width"] is not None:
                self.width = kwargs["width"]
            if "x" in kwargs and kwargs["x"] is not None:
                self.x = kwargs["x"]
            if "y" in kwargs and kwargs["y"] is not None:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            Returns the dictionary respresentation of the attributes
        """
        return {
                "x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
