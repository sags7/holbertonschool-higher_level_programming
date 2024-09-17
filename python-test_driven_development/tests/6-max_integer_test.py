#!/usr/bin/python3
"""
Unit test for max_integer([...])
"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        self.assertEqual(max_integer([2, 4, 6], 6))
        self.assertEqual(max_integer([-2, -4, 0], 0))
        self.assertEqual(max_integer([-2, -4, 5, 10], 10))

    def test_max_start(self):
        self.assertEqual(max_integer([0, -1, -100]), 0)
        self.assertEqual(max_integer([10, -1, -100]), 10)
        self.assertEqual(max_integer([100, 1, 10]), 100)

    def test_max_middle(self):
        self.assertEqual(max_integer([2, 100, 10]), 100)
        self.assertEqual(max_integer([-2, -1, -10]), -1)
        self.assertEqual(max_integer([2000, 25100, 10]), 25100)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, 1, 10]), 10)
        self.assertEqual(max_integer([1, -1, 10]), 10)
        self.assertEqual(max_integer([1, 10, -10]), 10)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-2, -1, -3]), -1)
        self.assertEqual(max_integer([-1, -200, -3]), -1)

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    if __name__ == "__main__":
        unittest.main()
