#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

"""
    Unittest for max_integer([..])
"""


class TestMaxInteger(unittest.TestCase):
    """
        Unit test for max integeri
    """
    def test_max_integer(self):
        result = max_integer([1, 3, 4, 6, 34, 3, 2, 0])
        self.assertEqual(result, 34)
        result = max_integer([1])
        self.assertEqual(result, 1)
