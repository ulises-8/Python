"""
CS3B, Assignment #6, Complex Numbers
Ulises Marian
testing
"""

import unittest
import copy

from assignment06 import *


class ComplexTestCase(unittest.TestCase):
    def setUp(self):
        self.c1 = Complex(1, 2)
        self.c2 = Complex(3, 4)

    def testAddComplex(self):
        """Test addition between 2 Complex"""
        expected = Complex(4, 6)
        actual = self.c1 + self.c2
        self.assertAlmostEqual(expected, actual)

    def testAddNumber(self):
        """Test adding a Complex and an int"""
        expected = Complex(2, 2)
        actual = 1 + self.c1
        self.assertAlmostEqual(expected, actual)

    def testRaddNumber(self):
        """Test adding an int and a Complex"""
        expected = Complex(2, 2)
        actual = self.c1 + 1
        self.assertAlmostEqual(expected, actual)

    def testAddFailure(self):
        """Test a Complex with something that cannot be added"""
        with self.assertRaises(TypeError):
            result = self.c1 + "rrr"

    #testing SUBTRACTION
    def testSubComplex(self):
        """Test subtraction between 2 Complex"""
        expected = Complex(-2, -2)
        actual = self.c1 - self.c2
        self.assertAlmostEqual(expected, actual)

    def testSubNumber(self):
        """Test subtracting ant and a Complex"""
        expected = Complex(0, -4)
        actual = 3 - self.c2
        self.assertAlmostEqual(expected, actual)

    def testRsubNumber(self):
        """Test subtracting a Complex and an int"""
        expected = Complex(1, 4)
        actual = self.c2 - 2
        self.assertAlmostEqual(expected, actual)

    def testSubFailure(self):
        """Test a Complex with something that cannot be subtracted"""
        with self.assertRaises(TypeError):
            result = self.c1 - "Salm0n"

    #testing MULTIPLICATION
    def testMulComplex(self):
        """Test multiplicating between 2 Complex"""
        expected = Complex(-5, 10)
        actual = self.c1 * self.c2
        self.assertAlmostEqual(expected, actual)

    def testMulNumber(self):
        """Test multiplicating a Complex and an int"""
        expected = Complex(21, 28)
        actual = self.c2 * 7
        self.assertAlmostEqual(expected, actual)

    def testRmulNumber(self):
        """Test multiplicating an int and a Complex"""
        expected = Complex(21, 28)
        actual = 7 * self.c2
        self.assertAlmostEqual(expected, actual)

    def testMulFailure(self):
        """Test a Complex with something that cannot be multiplied"""
        with self.assertRaises(TypeError):
            result = self.c1 * "YES s1r"

    #testing DIVISION
    def testTrueDivComplex(self):
        """Test dividing 2 Complex"""
        expected = Complex(.44, .08)
        actual = self.c1 / self.c2
        self.assertAlmostEqual(expected, actual)

    def testTrueDivNumber(self):
        """Test dividing a Complex by an int"""
        expected = Complex(0.5, 0.6666)
        actual = self.c2 / 6
        self.assertAlmostEqual(expected, actual)

    def testRtrueDivNumber(self):
        """Test dividing an int by a Complex"""
        expected = Complex(0.96, -1.28)
        actual = 8 / self.c2
        self.assertAlmostEqual(expected, actual)

    def testTrueDivFailure(self):
        """Test a Complex with something that cannot be divided"""
        with self.assertRaises(TypeError):
            result = self.c1 / "b3vit@min"

    #testing NEGATIVE
    def testNegComplex(self):
        """Complex negative"""
        expected = Complex(-1, -2)
        actual = -self.c1
        self.assertAlmostEqual(expected, actual)

    def testNegFailure(self):
        """" testing raising TypeError"""
        with self.assertRaises(TypeError):
            result = -Complex(5, "why?")

    #testing RECIPROCAL
    def testReciprocalComplex(self):
        expected = Complex(.12, -.16)
        actual = self.c2.reciprocal
        self.assertAlmostEqual(expected, actual)

    #testing reciprocal and abs
    def testRecAbsComplex(self):
        expected = Complex(.12, -.16)
        actual = self.c2.reciprocal.__abs__()
        self.assertAlmostEqual(expected, actual)

    def testReciprocalFailure(self):
        """Test reciprocal, raise TypeError"""
        with self.assertRaises(TypeError):
            result = Complex(7, "you").reciprocal


    #testing ABSOLUTE VALUE
    def testAbsComplex(self):
        expected = 5
        actual = self.c2.__abs__()
        self.assertAlmostEqual(expected, actual)

    #testing abs and reciprocal
    def testAbsRecComplex(self):
        expected = Complex(.2, .0)
        actual = Complex(self.c2.__abs__()).reciprocal
        self.assertAlmostEqual(expected, actual)

    def testAbsoluteFailure(self):
        """raising abs TypeError"""
        with self.assertRaises(TypeError):
            Complex("Thanks", 4).__abs__()

    # testing LT
    def testLessThanComplex(self):
        """complex < complex"""
        expected = True
        actual = self.c1 < self.c2
        self.assertEqual(expected, actual)

    def testLessThanComplex1(self):
        """complex < complex"""
        expected = False
        actual = self.c2 < self.c1
        self.assertEqual(expected, actual)

    def testNumLessThanComplex(self):
        """a real-number < complex"""
        expected = False
        actual = 6 < self.c2
        self.assertEqual(expected, actual)

    def testComplexLessThanNum(self):
        """complex < a real number"""
        expected = True
        actual = self.c2 < 6
        self.assertEqual(expected, actual)

    # test GreaterThan
    def testGreaterThanComplex(self):
        """complex > complex"""
        expected = True
        actual = self.c2 > self.c1
        self.assertEqual(expected, actual)

    def testGreaterThanNumber(self):
        """complex > number"""
        expected = True
        actual = self.c2 > 3
        self.assertEqual(expected, actual)

    def testNumberGreaterThanComplex(self):
        """number > complex"""
        expected = True
        actual = 9 > self.c2
        self.assertEqual(expected, actual)

    def testNumberGreaterThanComplex2(self):
        """number > complex"""
        expected = False
        actual = 4 > self.c2
        self.assertEqual(expected, actual)

    #testing EQ
    def testEqualComplex1(self):
        """ complex == complex...return False"""
        expected = False
        actual = self.c1 == self.c2   # false
        self.assertEqual(expected, actual)

    def testEqualComplex2(self):
        """complex == complex...return True"""
        expected = True
        actual = self.c1 == Complex(1, 2)  # true
        self.assertEqual(expected, actual)

    def testEqualComplex3(self):
        """complex == complex"""
        c3 = Complex(6, 0)
        expected = True
        actual = c3 == Complex(6)  # Complex(6) => Complex(6, 0)
        self.assertEqual(expected, actual)

    def testEqualComplex4(self):
        """complex == string... False"""
        expected = False
        actual = self.c2 == "8"
        self.assertEqual(expected, actual)

    def testEqualFailure(self):
        """string == complex... False"""
        expected = False
        actual = "HELLO" == self.c1
        self.assertEqual(expected, actual)


class ListsOfComplexCopies(unittest.TestCase):
    def setUp(self):
        self.list_complex = [Complex(3, 4), Complex(5, 6), Complex(7,8)]
        self.shallow = copy.copy(self.list_complex)
        self.deep = copy.deepcopy(self.list_complex)

    def testShallowCopy(self):
        """shallow copy IS NOT list_complex"""
        self.assertFalse(self.shallow is self.list_complex)  # indeed False

    def testElementsShallowCopy1(self):
        """shallow copy, copy of element[0]"""
        self.assertTrue(self.shallow[0] is self.list_complex[0])  #True

    def testElementsShallowCopy2(self):
        """shallow copy, copy of element[1]"""
        self.assertTrue(self.shallow[1] is self.list_complex[1])  # True

    def testElementsShallowCopy3(self):
        """shallow copy, copy of element[2]"""
        self.assertTrue(self.shallow[2] is self.list_complex[2])  # True

    # testing DeepCopy
    def testDeepCopy(self):
        """deepcopy is not list_complex"""
        self.assertFalse(self.deep is self.list_complex)  # indeed False

    def testElementsDeepCopy1(self):
        """testing copy of element[0]"""
        self.assertFalse(self.deep[0] is self.list_complex[0])  # indeed False

    def testElementsDeepCopy2(self):
        """testing copy of element[1]"""
        self.assertFalse(self.deep[1] is self.list_complex[1])  # indeed False

    def testElementsDeepCopy3(self):
        """testing copy of element[2]"""
        self.assertFalse(self.deep[2] is self.list_complex[2])  # indeed False





if __name__ == "__main__":
 unittest.main()