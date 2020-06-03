#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written
    Args: filename: string
    text: text to be written to
    """
    with open(filename, 'w') as my_file:
        return (my_file.write(text))
