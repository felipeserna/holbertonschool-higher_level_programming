#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout.
    Args: filename: string
    """
    with open(filename, encoding="utf-8") as my_file:
        text = my_file.read()
    print(text, end='')
