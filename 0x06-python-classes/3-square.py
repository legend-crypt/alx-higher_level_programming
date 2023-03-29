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
    def __init__(self, size=0):
        """
        This function initialize the class with a size of type int
        and also greater than 0

        Args:
            size (int): of  the square

        """
        self.set_size(size)

    def set_size(self, size):
        """
        This function sets the size with a value of int
        greater

        Args:
            size (int): should be an int and also greater than 0
        ValueError: when the size is less than 0
        TypeError: when the size is not an integer

        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: the area of the square
        """

        return self.__size * self.__size
print(help(Square))
