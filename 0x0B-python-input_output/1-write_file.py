#!/usr/bin/python3

"""
    No module was imported
"""


def write_file(filename="", text=""):
    """
        write a text to a file and also overwrite the
        content of the file if it already exitst
    """

    with open(filename, mode='w', encoding="utf-8") as file:
        text_len = file.write(text)
    return (text_len)
