"""
CS3B, Assignment #7, map, filter, reduce
Ulises Marian
Testing
"""

import unittest
from functools import reduce

from assignment07 import *

class MfrListTestCase(unittest.TestCase):
    def setUp(self):
        self.mfrlist = MfrList([12, 98, 25, 53, 12])
        self.tuplist = MfrList([("Zlatan", 19), ("Lukaku", 27), ("Messi", 33)])
        self.tuplist2 = MfrList([("Zlatan", 19)])
        self.caplist = MfrList(["hoy", "mañana", "Hoy", "mañAnA", "HOY"])
        self.palindlist = MfrList(["cake", "noon", "nun", "racecar"])
        self.onelist = MfrList([8])
        self.onelistel = MfrList(["bamboo"])
        self.emptylist = MfrList([])

    def testMap(self):
        #first test
        expected = self.mfrlist.map(lambda x:x * 2)
        actual = list(map(lambda x: x * 2, self.mfrlist))
        self.assertEqual(expected, actual)
        #second test
        expected = self.mfrlist.map(lambda x: x + 10)
        actual = list(map(lambda x: x + 10, self.mfrlist))
        self.assertEqual(expected, actual)
        #third test
        expected = self.mfrlist.map(lambda x: x - 11)
        actual = list(map(lambda x: x - 11, self.mfrlist))
        self.assertEqual(expected, actual)

    def testFilter(self):
        #first test
        expected = self.mfrlist.filter(lambda x: x % 2 == 1)
        actual = list(filter(lambda x: x % 2 == 1, self.mfrlist))
        self.assertEqual(expected, actual)
        #second test
        expected = self.mfrlist.filter(lambda x: x % 2 == 2)
        actual = list(filter(lambda x: x % 2 == 2, self.mfrlist))
        self.assertEqual(expected, actual)
        #third test
        expected = self.mfrlist.filter(lambda x: x == 12)
        actual = list(filter(lambda x: x == 12, self.mfrlist))
        self.assertEqual(expected, actual)

    def testReduce(self):
        #first test
        expected = self.mfrlist.reduce(lambda a, b: a + b)
        actual = reduce(lambda a, b: a + b, self.mfrlist)
        self.assertEqual(expected, actual)
        #second test
        expected = self.mfrlist.reduce(lambda a, b: a * b)
        actual = reduce(lambda a, b: a * b, self.mfrlist)
        self.assertEqual(expected, actual)
        #third test
        expected = self.mfrlist.reduce(lambda a, b: a if a < b else b)
        actual = reduce(lambda a, b:  a if a < b else b, self.mfrlist)
        self.assertEqual(expected, actual)

    def testCapitalize(self):
        #empty list
        expected = []
        actual = capitalize(self.emptylist)
        self.assertEqual(expected, actual)
        #single-element list
        expected = ['Bamboo']
        actual = capitalize(self.onelistel)
        self.assertEqual(expected, actual)
        #multiple-element list
        expected = ['Cake', 'Noon', 'Nun', 'Racecar']
        actual = capitalize(self.palindlist)
        self.assertEqual(expected, actual)

    def testBetween(self):
        #empty list
        expected = []
        actual = between(self.emptylist, 10, 40)
        self.assertEqual(expected, actual)
        #single-element list
        expected = [8]
        actual = between(self.onelist, 5, 10)
        self.assertEqual(expected, actual)
        #single-element list NOT within incl or excl
        expected = []
        actual = between(self.onelist, 9, 1000)
        self.assertEqual(expected, actual)
        #multiple-element list
        expected = [12, 25, 12]
        actual = between(self.mfrlist, 10, 40)
        self.assertEqual(expected, actual)
        # multiple-element list
        expected = [98]
        actual = between(self.mfrlist, 98, 99)
        self.assertEqual(expected, actual)
        expected = []
        actual = between(self.mfrlist, 99, 1000)
        self.assertEqual(expected, actual)

    def testOldest(self):
        # empty list
        with self.assertRaises(TypeError):
            result = oldest(self.emptylist)
        #single-element list
        expected = "Zlatan"
        actual = oldest(self.tuplist2)
        self.assertEqual(expected, actual)
        #multiple-element list
        expected = "Messi"
        actual = oldest(self.tuplist)
        self.assertEqual(expected, actual)

    def testJoin(self):
        #empty list
        expected = ""
        actual = join(self.emptylist, "-")
        self.assertEqual(expected, actual)
        #one-element list
        expected = "bamboo"
        actual = join(self.onelistel, "-")
        self.assertEqual(expected, actual)
        # multiple-element list
        expected = "cake-noon-nun-racecar"
        actual = join(self.palindlist, "-")
        self.assertEqual(expected, actual)

    def testSame(self):
        self.allequal = MfrList([7, 7, 7, 7, 7, 7])
        self.unequal = MfrList([7, 8, 7, 7, 7])
        self.allequall = MfrList(["PIZZA", "PIZZA", "PIZZA", "PIZZA"])
        self.notequal = MfrList(["Pizza", "PIZZA", "SODA"])
        #empty list
        expected = True
        actual = same(self.emptylist)
        self.assertEqual(expected, actual)
        # one-element list
        expected = True
        actual = same(self.onelistel)
        self.assertEqual(expected, actual)
        # all equal multiple-element list of numbers
        expected = True
        actual = same(self.allequal)
        self.assertEqual(expected, actual)
        # NOT equal multiple-element list of numbers
        expected = False
        actual = same(self.unequal)
        self.assertEqual(expected, actual)
        # all equal multiple-element list of strings
        expected = True
        actual = same(self.allequall)
        self.assertEqual(expected, actual)
        # NOT equal multiple-element list of strings
        expected = True
        actual = same(self.unequal)
        self.assertNotEqual(expected, actual)

    def testCountStr(self):
        #empty list
        expect = 0
        actual = count_str(self.emptylist, "key")
        self.assertEqual(expect, actual)
        # one-element list
        expect = 1
        actual = count_str(self.onelistel, "BAmBoO")
        self.assertEqual(expect, actual)
        # multiple-element list
        expect = 3
        actual = count_str(self.caplist, "hoy")
        self.assertEqual(expect, actual)
        # multiple-element list
        expect = 2
        actual = count_str(self.caplist, "MAÑANA")
        self.assertEqual(expect, actual)

    def testLongestPalindrome(self):
        palind = MfrList(["madam"])
        # empty list
        with self.assertRaises(TypeError):
            result = longest_palindrome(self.emptylist)
        #one-element list, NO palindrome
        with self.assertRaises(TypeError):
            result = longest_palindrome(self.onelistel)
        #one-element list, with palindrome
        expect = "madam"
        actual = longest_palindrome(palind)
        self.assertEqual(expect, actual)
        #multilpe-element list, with palindrome
        expect = "racecar"
        actual = longest_palindrome(self.palindlist)
        self.assertEqual(expect, actual)
        #multilpe-element list, NO palindrome
        with self.assertRaises(TypeError):
            longest_palindrome(self.caplist)














if __name__ == "__main__":
 unittest.main()