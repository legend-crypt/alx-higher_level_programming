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
    >>> print_square(3)
    ###
    ###
    ###

    >>> print_square(-6)
    Traceback (most recent call last):
    ValueError: size must be >= 0

    >>> print_square(2.2)
    Traceback (most recent call last):
    TypeError: size must be an integer

    >>> print_square("square")
    Traceback (most recent call last):
    TypeError: size must be an integer

	>>> print_square(0)


    >>> print_square()
    Traceback (most recent call last):
    TypeError: print_square() missing 1 required positional argument: 'size'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for r in range(size):
                print("#", end="")
            print()
