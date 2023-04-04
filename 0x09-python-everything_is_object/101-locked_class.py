#!/usr/bin/python3
"""
     No module was imported
"""


class LockedClass:
    """
        This prevents a user from dynamically creating new intances
        except only is the new instance is called first_name
    """
    __slots__ = ["first_name"]
