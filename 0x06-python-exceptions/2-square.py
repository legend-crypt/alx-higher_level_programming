#!/usr/bin/python3

class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0):
        """
        This function initialize the class with a size of type int
        and also greater than 0

        Args:
            size: of  the square
        """
        self.set_size = size

    def set_size(self, size):
        """
        This function sets the size
        Args:
            size: should be an int and also greater than 0
        """
        try:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
