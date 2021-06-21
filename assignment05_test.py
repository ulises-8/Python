"""
CS3C, Assignment #5, AVL tree
Ulises Marian
"""

from assignment05 import *
from bst_test import *
import random


class AvlTreeTestCase(BstTestCase):
    TreeType = AvlTree

    def testAvlTreeRepr(self):
        print(repr(self.tree))

    def testRotateRightLLDemo(self):
        avltree = self.TreeType()
        data = [3, 2, 1]
        for d in data:
            avltree.insert(d)

        print(avltree)
        self.assertEqual(2, avltree._root.data)
        self.assertEqual(1, avltree._root.left_child.data)
        self.assertEqual(3, avltree._root.right_child.data)

        self.assertEqual(1, avltree._root.height)
        self.assertEqual(0, avltree._root.left_child.height)
        self.assertEqual(0, avltree._root.right_child.height)

    def testRotateLeft(self):
        avltree = self.TreeType()
        data = [1, 2, 3]
        for d in data:
            avltree.insert(d)

        print(avltree)
        self.assertEqual(2, avltree._root.data)
        self.assertEqual(1, avltree._root.left_child.data)
        self.assertEqual(3, avltree._root.right_child.data)

        self.assertEqual(1, avltree._root.height)
        self.assertEqual(0, avltree._root.left_child.height)
        self.assertEqual(0, avltree._root.right_child.height)

    def testLeftRightRotation(self):
        avltree = self.TreeType()
        data = [3,1,2]
        for d in data:
            avltree.insert(d)
            print(d)

        print(avltree)
        self.assertEqual(2, avltree._root.data)
        self.assertEqual(1, avltree._root.left_child.data)
        self.assertEqual(3, avltree._root.right_child.data)

        self.assertEqual(1, avltree._root.height)
        self.assertEqual(0, avltree._root.left_child.height)
        self.assertEqual(0, avltree._root.right_child.height)

    def testRightLeftRotation(self):
        avltree = self.TreeType()
        data = [1,3,2]
        for d in data:
            avltree.insert(d)
            print(d)

        print(avltree)
        self.assertEqual(2, avltree._root.data)
        self.assertEqual(1, avltree._root.left_child.data)
        self.assertEqual(3, avltree._root.right_child.data)

        self.assertEqual(1, avltree._root.height)
        self.assertEqual(0, avltree._root.left_child.height)
        self.assertEqual(0, avltree._root.right_child.height)

    def testRemove(self):
        avltree = self.TreeType()
        data = [1, 3, 2, 5, 6]
        for d in data:
            avltree.insert(d)
        print(avltree)

        avltree.remove(5)
        avltree.remove(2)
        print(avltree)
        avltree.remove(1)
        print(avltree)
        avltree.remove(3)
        print(avltree)
        avltree.remove(6)
        print(avltree)

        print(avltree)

    def assertIsAvlTree(self, subtree_root):
        if subtree_root._root is not None:
            self.assertIsInstance(subtree_root._root, AvlTreeNode)
            height = self.setting_height(subtree_root._root)
            print(f"height is: {height}")
            self.checking_order(subtree_root._root)

    def testTraversal(self):
        avltree = self.TreeType()
        data = random.sample(range(1, 300), 110)
        for d in data:
            avltree.insert(d)
            self.assertIsAvlTree(avltree)  #The height,after inserting 110
                                            #numbers varies between 7 and 8
                                            #which is what I expected, after
                                            #having tested it with different
                                            #amount of numbers
        print(avltree)
        new_list = []
        random.shuffle(data)
        for num in data:
            print("removing", num)
            avltree.remove(num)
            print(avltree)
            self.assertIsAvlTree(avltree)

    def setting_height(self, subtree_root, height=0):
        if subtree_root is None:
            return height-1

        height = 1 + max(self.setting_height(subtree_root.left_child),
                         self.setting_height(subtree_root.right_child))
        self.assertEqual(height, subtree_root.height)
        return height

    def checking_order(self, subtree_root):
        if subtree_root is None:
            return
        if subtree_root.left_child is None and subtree_root.right_child is None:
            return
        self.less_than(subtree_root.left_child, subtree_root.data)
        self.greater_than(subtree_root.right_child, subtree_root.data)
        self.checking_order(subtree_root.left_child)
        self.checking_order(subtree_root.right_child)

    def less_than(self, subtree_root, value):
        if subtree_root is None:
            return
        self.assertTrue(subtree_root.data < value)
        self.less_than(subtree_root.left_child, value)
        self.less_than(subtree_root.right_child, value)

    def greater_than(self, subtree_root, value):
        if subtree_root is None:
            return
        self.assertTrue(subtree_root.data > value)
        self.greater_than(subtree_root.left_child, value)
        self.greater_than(subtree_root.right_child, value)







del BstTestCase