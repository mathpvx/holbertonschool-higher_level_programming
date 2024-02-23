#!/usr/bin.python3
"""
    Module of test
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        self.base = Base(12)

    def test_nb_objects(self):
        # test nb_object before first call
        Base.__nb_objects = 0

    def test_ID(self):
        # if id, id = value
        base = Base(39)
        self.assertEqual(base.id, 39)

    def test_IDNone(self):
        # if no id, id = nb_obj
        base1 = Base()
        self.assertEqual(base1.id, 1)


class TestBaseStaticMethod(unittest.TestCase):

    def setUp(self):
        self.base = Base(12)

    def test_outputTypeToJsonString(self):
        # test output function is a string
        list_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(type(Base.to_json_string(list_dict)), str)

    def test_outputEmptyToJsonString(self):
        # test output function if None as input is a string empty list
        list_dict = None
        self.assertEqual(Base.to_json_string(list_dict), '[]')

    def test_outputTypeFromJsonString(self):
        # test output function is a list
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(type(Base.from_json_string(json_string)), list)

    def test_outputEmptyTypeFromJsonString(self):
        # test output function if None as input is a empty list
        json_string = None
        self.assertEqual(Base.from_json_string(json_string), [])


if __name__ == '__main__':
    unittest.main()
