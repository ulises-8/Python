"""
CS3C, Assignment #4, lazy-delete binary tree tests
Ulises Marian
"""

from assignment04 import *
from bst_test import *


# Inherit from the basic BST tests so all those should run.
class LazyBinarySearchTreeTestCase(BstTestCase):
    # Override class variable so all existing tests instantiate and test
    # LazyBinarySearchTree instead of BinarySearchTree
    TreeType = LazyBinarySearchTree

    # TODO add tests specifically for LazyBinarySearchTree
    def setUp(self):
        self.tree = self.TreeType()
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(5)
        self.tree.insert(8)
        self.tree.remove(20)
        self.tree.insert(44)
        self.tree.insert(60)
        self.tree.remove(44)
        self.tree.remove(5)
        #print(self.tree)

    def testFind(self):
        expected = 10
        actual = self.tree.find(10)
        self.assertEqual(expected, actual)

        #expected = 8
        #actual = self.tree.find(8)
        #self.assertEqual(expected, actual)

        expected = 60
        actual = self.tree.find(60)
        self.assertEqual(expected, actual)

        with self.assertRaises(BinarySearchTree.NotFoundError):
            self.tree.find(5)
        with self.assertRaises(BinarySearchTree.NotFoundError):
            self.tree.find(44)
        with self.assertRaises(BinarySearchTree.NotFoundError):
            self.tree.find(20)

    def testFindMin(self):
        expected = 8
        actual = self.tree.find_min()
        self.assertEqual(expected, actual)

        self.tree.insert(3)
        expected = 3
        actual = self.tree.find_min()
        self.assertEqual(expected, actual)

        self.tree.insert(2)
        expected = 2
        actual = self.tree.find_min()
        self.assertEqual(expected, actual)


    def testFindMax(self):
        expected = 60
        actual = self.tree.find_max()
        self.assertEqual(expected, actual)

        self.tree.insert(100)
        expected = 100
        actual = self.tree.find_max()
        self.assertEqual(expected, actual)

        self.tree.insert(102)
        expected = 102
        actual = self.tree.find_max()
        self.assertEqual(expected, actual)

    def testIter(self):
        tree1 = self.TreeType()
        data = [9, 6, 55, 33, 70, 81]
        for d in data:
            tree1.insert(d)

        tree1.remove(55)
        tree1.remove(33)
        tree1.remove(9)
        tree1.remove(70)


        expected = [6, 9, 33, 55, 70, 81]
        generator = tree1.__iter__(True)
        actual = []
        for num in generator:
            actual.append(num)
        self.assertEqual(expected, actual)

        tree2 = self.TreeType()
        data = [4, 77, 11, 3, 98, 52, 62, 2, 33333]
        for d in data:
            tree2.insert(d)

        tree2.remove(77)
        tree2.remove(4)
        tree2.remove(33333)
        tree2.remove(98)
        tree2.remove(11)
        tree2.remove(62)

        expected = sorted(data)
        generator = tree2.__iter__(True)
        actual = []
        for num in generator:
            actual.append(num)
        self.assertEqual(expected, actual)

    def testCollectGarbage(self):
        tree1 = self.TreeType()
        data = [8, 4, 85, 73, 90, 23]
        for d in data:
            tree1.insert(d)

        tree1.remove(23)
        tree1.remove(85)
        tree1.remove(90)

        tree1.collect_garbage()

        s =""
        s += "size=3" + "\n"
        s += "    73" + "\n"
        s += "8" + "\n"
        s += "    4" + "\n"

        expected = s
        actual = tree1.__str__()
        self.assertEqual(expected, actual)







# Remove BstTestCase so it doesn't run against BinarySearchTree
del BstTestCase

if __name__ == '__main__':
    unittest.main()
