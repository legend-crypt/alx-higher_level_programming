#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    This class defines a square of private instance `size`
    raises a ValueError when the size is less than 0 and
    typeerror when the size is not an integer
    """
    def __init__(self, value=0):
        """
        This function initialize the class with a size of type int
        and also greater than 0

        Args:
            size (int): of  the the size of the square

        """
        self.size = value

    @property
    def size(self):
        """
        This a getter method for getting the size of the
        square
        Return:
            int: the size of the square
        """
        return self.__value

    @size.setter
    def size(self, value):
        """
        This function sets the size with a value of int
        greater

        Args:
            size (int): should be an int and also greater than 0
        ValueError: when the size is less than 0
        TypeError: when the size is not an integer

        """
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
            elif isinstance(value, float):
                raise TypeError("size must be an integer")
            else:
                self.__value = value
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Returns the area of the square

        Returns:
            int: the area of the square
        """

        return self.__value * self.__value
