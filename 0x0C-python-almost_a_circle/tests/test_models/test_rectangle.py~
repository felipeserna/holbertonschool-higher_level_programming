#!/usr/bin/python3
"""Unittest for Almost a circle
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tests class Base
    """
    def setUp(self):
        """set the start point"""

        Base.Base__nb_objects = 0

    def test_01(self):
        """test for task 1"""

        base0 = Base()
        base1 = Base()
        base2 = Base(13)
        base3 = Base("felipe")
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)
        self.assertEqual(base2.id, 13)
        self.assertEqual(base3.id, "felipe")

if __name__ == '__main__':
    unittest.main()
