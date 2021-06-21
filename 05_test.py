"""
CS3B, Assignment #5, Logic gate simulation (Part 2)
Ulises Marian
Testing full-adder
"""

import unittest

from Assignment05 import *

class Full_Adder(unittest.TestCase):
    def test_full_adder(self):
        actual = full_adder(True, False, True)
        expected = (False, True, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(True, True, False)
        expected = (False, True, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(True, True, True)
        expected = (True, True, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(False, True, True)
        expected = (False, True, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(False, False, True)
        expected = (True, False, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(False, False, False)
        expected = (False, False, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(True, False, False)
        expected = (True, False, 450)
        self.assertEqual(expected, actual)

    def test_full_adder(self):
        actual = full_adder(False, True, False)
        expected = (True, False, 450)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
