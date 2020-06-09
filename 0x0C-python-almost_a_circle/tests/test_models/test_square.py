#!/usr/bin/python3
"""Unittest for Almost a circle
"""
import unittest
from models.square import Square
import sys
from io import StringIO
import pep8
from models import square


class TestSquareDocs(unittest.TestCase):
    """ checking for documentation """
    def test_module_doc(self):
        """ checking for module documentation """
        self.assertTrue(len(square.__doc__) > 0)

    def test_class_doc(self):
        """ checking for class documentation """
        self.assertTrue(len(Square.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method documentation """
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)


class TestSquarePep8(unittest.TestCase):
    """ checking for pep8 validation """
    def test_pep8(self):
        """ testing square and test_square for pep8 """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/square.py'
        file2 = 'tests/test_models/test_square.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


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
