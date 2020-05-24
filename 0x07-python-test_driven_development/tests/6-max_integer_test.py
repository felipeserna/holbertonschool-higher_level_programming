#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    tests the maximum integer
    """
    def test_with_integers(self):
        """tests with integer values"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-5, -30, -15, -23]), -5)
        self.assertEqual(max_integer([3.4, -2.1]), 3.4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([float('inf'), 3]), float('inf'))
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1.3, 23, 10, 90.1, 90.2]), 90.2)
        self.assertEqual(max_integer([1]), 1)

    def test_with_strings(self):
        """tests with strings values"""
        self.assertEqual(max_integer("holberton"), 't')
        self.assertEqual(max_integer("ABabcCzZ234"), 'z')
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_errors(self):
        """raises errors from max_integer"""
        self.assertRaises(TypeError, max_integer, [5j, 3j])
        self.assertRaises(TypeError, max_integer, 25)
