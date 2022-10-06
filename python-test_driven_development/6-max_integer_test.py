#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test file for the function Max_integer()
    in different cases"""
    def test_maxint(self):
        # Test max_integer when list >= 0
        self.assertAlmostEqual(max_integer([6]), 6)
        self.assertAlmostEqual(max_integer([6, 3, 4]), 6)
        self.assertAlmostEqual(max_integer([6, 2, 7, 8]), 8)
        self.assertAlmostEqual(max_integer([-10, 34, 12, 15]), 34)
        self.assertAlmostEqual(max_integer([-2, -7, -9, -10]), -2)
        self.assertAlmostEqual(max_integer([]), None)
