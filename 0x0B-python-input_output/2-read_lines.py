#!/usr/bin/python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout
    Args: filename: string
    nb_lines: lines to be read
    """
    total_lines = 0
    with open(filename, encoding="utf-8") as my_file:
        for i in my_file:
            total_lines = total_lines + 1
            if nb_lines <= 0 or nb_lines >= total_lines:
                print(i, end='')
