#!/usr/bin/python3
"""Unittest for Almost a circle
"""
import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
import pep8
import sys
import io
from models import base


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8B(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


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

    def test_15(self):
        """test for task 15"""

        r1 = Rectangle(10, 7, 2, 8)
        dict_1 = r1.to_dictionary()
        r2 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dict_1, r2])
        python_dictionary = json.loads(json_dictionary)
        self.assertEqual([dict_1, r2], python_dictionary)

        Empty = Base.to_json_string(None)
        self.assertEqual(Empty, "[]")

        Empty2 = Base.to_json_string([])
        self.assertEqual(Empty2, "[]")

if __name__ == '__main__':
    unittest.main()
