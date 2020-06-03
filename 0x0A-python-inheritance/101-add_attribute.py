#!/usr/bin/python3
"""Can I?"""


def __add__(self, value):
    """adds a new attribute to an object"""
    if value:
        raise TypeError("can't add new attribute")
