#!/usr/bin/python3

"""
    No module was imported
"""


def append_write(filename="", text=""):
    """
        write a text to a file and also append to the
        content of the file if it already exits
    """

    with open(filename, mode='a', encoding="utf-8") as file:
        text_len = file.write(text)
    return (text_len)
