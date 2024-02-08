#!/usr/bin/python3
"""
    unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class for unittests """
    def test_max_integer(self):
        """ check possible cases edge cases """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([15, 10, 5]), 15)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)

    def test_type_error(self):
        """ type_errors """
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])
