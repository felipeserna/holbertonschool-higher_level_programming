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
        self.square = Square(2, 2, 2, 2)
        sys.stdout = StringIO()

    def test_14(self):
        """test for task 14"""
        s1 = Square(3, 4, 5, 6)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict,
                         {'y': 5, 'id': 6, 'size': 3, 'x': 4})


if __name__ == '__main__':
    unittest.main()
