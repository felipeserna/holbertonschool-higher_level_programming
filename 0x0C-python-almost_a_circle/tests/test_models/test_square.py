#!/usr/bin/python3
"""Unittest for Almost a circle
"""
import unittest
from models.square import Square
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """
    tests class Square
    """
    def setUp(self):
        """set the start point"""
        self.square = Square(2, 2, 3, 4, 5)
        sys.stdout = StringIO()


if __name__ == '__main__':
    unittest.main()
