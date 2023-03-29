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
    def __init__(self, value=0, pos_value=(0, 0)):
        """
        This function initialize the class with a size of type int
        and also greater than 0

        Args:
            size (int): of  the the size of the square
            position (tuple): the position of the square

        """
        self.size = value
        self.position = pos_value

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

    @property
    def position(self):
        """
        Retrieve the position
        Return:
            tuple: the positon
        """
        return self.__pos_value

    @position.setter
    def position(self, pos_value=(0, 0)):
        """
        Set the position of the the square based the value
        inputed with 2 positive intergers
        Raises:
            TypeError: if position is not a value of two
                        positive tuples
        """
        try:
            if pos_value[0] or pos_value[1] < 0:
                raise TypeError("position must be a tuple of positive integers")
            elif len(pos_value) < 2:
                raise TypeError("postion must be a tupele of 2 positive integers")
            else:
                self.__pos_value = pos_value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Returns the area of the square

        Returns:
            int: the area of the square
        """

        return self.__value * self.__value

    def my_print(self):
        """
        This function square with #
        if the size is 0 it will an empty line
        """

        if self.__value == 0:
            print("")
        else:
            for i in range(self.__value):

                for k in range(self.__value):
                    print("#", end="")
                print("")
