#!/usr/bin/python3

import sys

"""
    This module print to stdout, stderr and stdin
"""


def safe_print_integer_err(value):
    """
        This function print value return is aguement is int and false
        if not int and error message to stderr
        Aguement:
            value (int): take in an interger
            Raise:
                TypeError: if value is not int
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
