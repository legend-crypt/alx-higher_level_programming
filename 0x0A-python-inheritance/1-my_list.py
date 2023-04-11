#!/usr/bin/python3

"""
    No module was imported
"""


class MyList(list):
    """
        inherit from a list and print a sorted list
    """

    def print_sorted(self):
        """
            print a sorted list
        """
        print(sorted(self))
