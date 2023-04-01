#!/usr/bin/python3


import sys
"""
    This module prints to stderr
"""


def safe_function(fct, *args):
    """
        This function return the result of a passed in fuction
        it returns None if an Exception occurs

        Args:
            fct: a passed in function
            args: the aguements passed into the function
    """

    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
