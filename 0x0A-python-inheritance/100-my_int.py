#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """inherits from int"""

    def __ne__(self, value):
        """Args:
        value: integer
        """
        return super().__eq__(value)

    def __eq__(self, value):
        """value: integer"""
        return super().__ne__(value)
