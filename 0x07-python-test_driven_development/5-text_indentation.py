#!/usr/bin/python3
"""
prints a text with 2 new lines
after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """
    Args: text: string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    characters = [':', '.', '?']
    start_of_line = True

    for i in text:
        if i == ' ' and start_of_line is True:
            continue
        if i in characters:
            print(i, end='')
            print('\n')
            start_of_line = True
        else:
            print(i, end='')
            start_of_line = False
