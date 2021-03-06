#!/usr/bin/python3
"""Unittest for Almost a circle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
import pep8
from models import rectangle


class TestRecDocs(unittest.TestCase):
    """ checking for documentation """
    def test_module_doc(self):
        """ checking for module documentation """
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ checking for class documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method documentation """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


class TestRectanglePep8(unittest.TestCase):
    """ checking for pep8 validation """
    def test_pep8(self):
        """ test rectangle and test_rectangle
            for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/rectangle.py'
        file2 = 'tests/test_models/test_rectangle.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestRectangle(unittest.TestCase):
    """
    tests class Rectangle
    """
    def setUp(self):
        """set the start point"""
        self.rectangle = Rectangle(2, 2, 2, 2, 3)
        sys.stdout = StringIO()

    def tearDown(self):
        """clean everything up after running setup"""
        sys.stdout = sys.__stdout__

    def test_03(self):
        """test for task 3"""
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 2)
        self.assertEqual(self.rectangle.id, 3)

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

    def test_04(self):
        """test for task 4"""
        self.assertEqual(self.rectangle.area(), 4)

        r1 = Rectangle(2, 4, 0, 0, 1)
        self.assertEqual(r1.area(), 8)

    def test_05(self):
        """test for task 5"""
        r4 = Rectangle(2, 2)
        str_r4 = '##\n' \
                 '##\n'

        try:
            r4.display()
            self.assertEqual(sys.stdout.getvalue(), str_r4)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_06(self):
        """test for task 6"""
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (3) 2/2 - 2/2")
        r2 = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(r2.__str__(), "[Rectangle] (7) 5/6 - 3/4")
        r3 = Rectangle(8, 9, 3, 3, 3)
        self.assertEqual(r3.__str__(), "[Rectangle] (3) 3/3 - 8/9")

    def test_07(self):
        """test for task 7"""
        r5 = Rectangle(2, 2, 2, 2, 8)
        str_r5 = '\n\n  ##\n  ##\n'

        try:
            r5.display()
            self.assertEqual(sys.stdout.getvalue(), str_r5)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_08(self):
        """test for task 8"""
        r6 = Rectangle(1, 2, 3, 4, 5)
        r6.update(6, 7, 8, 9, 0)
        self.assertEqual(r6.__str__(), "[Rectangle] (6) 9/0 - 7/8")

    def test_09(self):
        """test for task 9"""
        r7 = Rectangle(3, 1, 9, 5, 3)
        r7.update(height=4, y=4, x=4, id=4, width=4)
        self.assertEqual(r7.__str__(), "[Rectangle] (4) 4/4 - 4/4")

    def test_13(self):
        """test for task 13"""
        r8 = Rectangle(4, 5, 9, 4, 3)
        r8_dict = r8.to_dictionary()
        self.assertEqual(r8_dict,
                         {'y': 4, 'width': 4, 'x': 9, 'id': 3, 'height': 5})


if __name__ == '__main__':
    unittest.main()
