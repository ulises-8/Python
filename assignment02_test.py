"""
CS3C, Assignment #2, Sparse Matrices
Ulises Marian
unittest
"""

from assignment02 import *
import unittest

class SparseMatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.matrix = SparseMatrix(20, 15, 0)

    def testDefaultValue(self):
        expected = 0
        actual = self.matrix.get(6, 7)
        self.assertEqual(expected, actual)

        expected = 0
        actual = self.matrix.get(10, 1)
        self.assertEqual(expected, actual)

        expected = 0
        actual = self.matrix.get(3, 13)
        self.assertEqual(expected, actual)

    def testGetValue(self):
        self.matrix.set(10, 10, 7)
        expected = 7
        actual = self.matrix.get(10, 10)
        self.assertEqual(expected, actual)

        self.matrix.set(10, 10, 44)
        expected = 44
        actual = self.matrix.get(10, 10)
        self.assertEqual(expected, actual)

        self.matrix.set(4, 6, 22)
        expected = 22
        actual = self.matrix.get(4, 6)
        self.assertEqual(expected, actual)

        self.matrix.set(4, 6, 33)
        expected = 33
        actual = self.matrix.get(4, 6)
        self.assertEqual(expected, actual)

        self.matrix.set(4, 6, 22)
        expected = 22
        actual = self.matrix.get(4, 6)
        self.assertEqual(expected, actual)

        self.matrix.set(1, 1, 8)
        expected = 8
        actual = self.matrix.get(1, 1)
        self.assertEqual(expected, actual)

        self.matrix.set(1, 1, 2)
        expected = 2
        actual = self.matrix.get(1, 1)
        self.assertEqual(expected, actual)

    def testGetRaiseIndexError(self):
        with self.assertRaises(IndexError):
            self.matrix.get(30, 4)

        with self.assertRaises(IndexError):
            self.matrix.get(22, 10)

        with self.assertRaises(IndexError):
            self.matrix.get(5, 40)

    def testSetRaiseIndexError(self):
        with self.assertRaises(IndexError):
            self.matrix.set(21, 21, 8)

        with self.assertRaises(IndexError):
            self.matrix.set(90, 10, 9)

        with self.assertRaises(IndexError):
            self.matrix.set(33, 7, 77)

    def testGetRow(self):
        #test 1
        self.matrix.set(3, 3, 9)
        self.matrix.set(3, 14, 55)
        self.matrix.set(3, 11, 11)
        expected = [9, 11, 55]
        generator = self.matrix.get_row(3)
        actual = []
        for num in generator:
            actual.append(num)
        self.assertEqual(expected, actual)

        #test 2
        self.matrix.set(9, 2, 6666)
        self.matrix.set(9, 7, 554)
        self.matrix.set(9, 11, 8)
        self.matrix.set(9, 4, 515)
        self.matrix.set(9, 6, 232)
        expected = [8, 232, 515, 554, 6666]
        generator = self.matrix.get_row(9)
        actual = []
        for num in generator:
            actual.append(num)
        self.assertEqual(expected, actual)


    def testGetCol(self):
        # test 1
        self.matrix.set(3, 4, 32)
        self.matrix.set(5, 4, 1)
        self.matrix.set(8, 11, 76)
        self.matrix.set(9, 4, 300)
        self.matrix.set(16, 4, 101)
        expected = [32, 1, 300, 101]
        generator = self.matrix.get_col(4)
        actual = []
        for num in generator:
            actual.append(num)
        self.assertEqual(expected, actual)

        # test 2
        self.matrix.set(1, 6, 656)
        self.matrix.set(2, 6, 21)
        self.matrix.set(3, 6, 45)
        self.matrix.set(13, 6, 67)
        self.matrix.set(4, 6, 768)
        expected = [656, 21, 45, 768, 67]
        generator = self.matrix.get_col(6)
        actual = []
        for num in generator:
            actual.append(num)
        self.assertEqual(expected, actual)


    def testGetRowColIndexError(self):
        # row
        with self.assertRaises(IndexError):
            self.matrix.get_row(30)
        # row
        with self.assertRaises(IndexError):
            self.matrix.get_row(21)
        # row
        with self.assertRaises(IndexError):
            self.matrix.get_row(100)

        # col
        with self.assertRaises(IndexError):
            self.matrix.get_col(16)
        # col
        with self.assertRaises(IndexError):
            self.matrix.get_col(20)
        # col
        with self.assertRaises(IndexError):
            self.matrix.get_col(40)

    def testStr(self):
        small_matrix = SparseMatrix(7, 7, 0)
        small_matrix.set(2, 2, 8)
        small_matrix.set(2, 3, 1)
        small_matrix.set(0, 3, 3)
        small_matrix.set(1, 0, 7)
        small_matrix.set(6, 4, 9)
        small_matrix.set(3, 6, 6)
        small_matrix.set(2, 5, 5)
        small_matrix.set(5, 1, 4)
        actual = small_matrix.__str__()
        expected = "0 0 0 3 0 0 0 \n" \
                   "7 0 0 0 0 0 0 \n" \
                   "0 0 8 1 0 5 0 \n" \
                   "0 0 0 0 0 0 6 \n" \
                   "0 0 0 0 0 0 0 \n" \
                   "0 4 0 0 0 0 0 \n" \
                   "0 0 0 0 9 0 0 \n"
        self.assertEqual(expected, actual)

        #__str__() with parameters - partial matrix
        actual = small_matrix.__str__(2, 2, 4, 5)
        expected = "8 1 0 5 0 \n" \
                   "0 0 0 0 6 \n" \
                   "0 0 0 0 0 \n" \
                   "0 0 0 0 0 \n"
        self.assertEqual(expected, actual)

        # __str__() with parameters - partial matrix outside matrix
        actual = small_matrix.__str__(5, 1, 20, 700)
        expected = "4 0 0 0 0 0 \n" \
                   "0 0 0 9 0 0 \n"
        self.assertEqual(expected, actual)

    def testClear(self):
        matrix = SparseMatrix(16, 16, 0)
        matrix.set(3, 4, 6)
        matrix.set(10, 15, 20)
        matrix.set(5, 14, 100)
        print(matrix)
        matrix.clear()
        print(matrix)