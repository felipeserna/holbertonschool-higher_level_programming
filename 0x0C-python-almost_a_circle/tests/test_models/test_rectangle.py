#!/usr/bin/python3
"""Unittest for Almost a circle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    tests class Rectangle
    """
    def setUp(self):
        """set the start point"""
        self.rectangle = Rectangle(2, 2, 2, 2, 3)

    def test_03(self):
        """test for task 3"""
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 2)
        self.assertEqual(self.rectangle.height, 2)

        r0 = Rectangle(10, 2, 3, 0, 4)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 0)

    def test_errors_03(self):
        """test errors for task 3"""
        self.assertRaises(TypeError, Rectangle, 5j, 3, 1, 1)
        self.assertRaises(TypeError, Rectangle, 5, "felipe", 1, 1, 3)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, float('inf'), 3, 1, 1)
        self.assertRaises(TypeError, Rectangle, (2, 4), 3, 1, 1)
        self.assertRaises(TypeError, Rectangle, 3, 3, 3j, 4)
        self.assertRaises(TypeError, Rectangle, 5, {3}, 1, 1)

        self.assertRaises(ValueError, Rectangle, -5, 3, 1, 1)
        self.assertRaises(ValueError, Rectangle, 0, 3, 1, 1)
        self.assertRaises(ValueError, Rectangle, 5, 3, 1, -1)


if __name__ == '__main__':
    unittest.main()
