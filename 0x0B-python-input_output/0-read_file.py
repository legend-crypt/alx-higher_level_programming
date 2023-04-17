#!/usr/bin/python3

"""
    No module was imported
"""


def read_file(filename=""):
    """
        Read text in a file line by line

        Args:
            filename(file): a the file we are reading from
    """

    with open(filename, encoding="utf-8") as file:

        for line in file:
            print(line, end="")
