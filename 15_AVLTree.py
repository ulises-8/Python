"""
CS3C, Assignment #5, AVL tree
Ulises Marian
"""

from bst import *
import random

class AvlTreeNode(BinaryTreeNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 0

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __repr__(self):
        return super().__repr__() + f", height={self.height}"

    @property
    def child_heights(self):
        # If there's a child, even if it's just one node, its height is 0.  so
        # if there's no child, the height should be -1.
        left_height = self.left_child.height if self.left_child else -1
        right_height = self.right_child.height if self.right_child else -1
        return left_height, right_height

    def adjust_height(self):
        self.height = 1 + max(self.child_heights)

class AvlTree(BinarySearchTree):
    # Override TreeNode, which is used in BinarySearchTree._insert() to create
    # a new node
    TreeNode = AvlTreeNode

    # Height of the tree, which is the height of root if it's not empty
    @property
    def height(self):
        if self._root:
            return self._root.height
        else:
            return -1

    def _insert(self, subtree_root, data):
        subtree_root = super()._insert(subtree_root, data)
        subtree_root.adjust_height()
        subtree_root = self._rotate(subtree_root)
        return subtree_root

    def _rotate_right(self, subtree_root):
        lc = subtree_root.left_child
        subtree_root.left_child = lc.right_child
        lc.right_child = subtree_root
        subtree_root.adjust_height()
        lc.adjust_height()
        return lc

    def _rotate_left(self, subtree_root):
        rc = subtree_root.right_child
        subtree_root.right_child = rc.left_child
        rc.left_child = subtree_root
        subtree_root.adjust_height()
        rc.adjust_height()
        return rc

    def _rotate(self, subtree_root):
        left_height, right_height = subtree_root.child_heights

        diff_left = left_height - right_height
        diff_right = right_height - left_height

        #check left-right
        if diff_left > 1:
            if subtree_root.left_child.child_heights[0] < 0:
                subtree_root.left_child = self._rotate_left(subtree_root.left_child)
                return self._rotate_right(subtree_root)
            else: #left-left
                return self._rotate_right(subtree_root)

        #check right-left
        elif diff_right > 1:
            if subtree_root.right_child.child_heights[1] < 0:
                subtree_root.right_child = self._rotate_right(subtree_root.right_child)
                return self._rotate_left(subtree_root)
            else: #right-right
                return self._rotate_left(subtree_root)

        return subtree_root

    def remove(self, data):
        self._root = self._removal(self._root, data)

    def _removal(self, subtree_root, data):
        subtree_root = super()._remove(subtree_root, data)
        if subtree_root is not None:
            self.adjust_all_heights()
            subtree_root.adjust_height()
            subtree_root = self._rotate(subtree_root)
        return subtree_root

    def _set_height(self, subtree_root):
        if not subtree_root:
            return -1
        else:
            subtree_root.height = 1 + max(self._set_height(
                subtree_root.left_child),
                           self._set_height(subtree_root.right_child))
            return subtree_root.height

    def adjust_all_heights(self):
        self._set_height(self._root)


def main():
    tree = AvlTree()
    tree.insert(0)
    tree.insert(1)
    tree.insert(7)
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)

    print(tree)

main()
