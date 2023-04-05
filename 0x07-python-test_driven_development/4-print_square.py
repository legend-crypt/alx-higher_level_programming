#!/usr/bin/python3

"""
    No module was imported
"""


def print_square(size):
    """
        Print a square using # with the size
        specified in the function parameter `size`

        Args:
            size (int): the size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        if size == 0:
            print()
        for i in range(size):
            for r in range(size):
                print("#", end="")
            print()
