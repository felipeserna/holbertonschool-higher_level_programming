#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text
    file (UTF8) and returns the number of characters added
    Args: filename: string
    text: text to be appended to
    """
    with open(filename, 'a') as my_file:
        return (my_file.write(text))
