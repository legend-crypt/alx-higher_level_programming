#!/usr/bin/python3

"""
    No module was imported
"""


def text_indentation(text):
    """
        print a text and indented manner
        moves to next when `.`, `?`, `:`
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if i == '.' or i == '?' or i == ':':
            print("")
            print("")
