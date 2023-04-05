#!/usr/bin/python3

"""
    No module was imported
"""


class Rectangle:

    number_of_instances = 0

    """
        This class define a rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """
            Sets up the class
            with a width and height

            Args:
                width (int): the widthe of the rectangle
                height (int): the height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
            calculates the area of rectangle and return it
        """
        return self.width * self.height

    def perimeter(self):
        """
            calculates the perimeter of the rectangle and return it

        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):

        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                rect += "#" * self.width
                if i == self.height - 1:
                    break
                rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
