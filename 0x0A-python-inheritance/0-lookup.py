#!/usr/bin/python3
"""
returns the list of
available attributes and
methods of an object
"""


def lookup(obj):
    """
    Args: obj: object.
    """
    return(dir(obj))
