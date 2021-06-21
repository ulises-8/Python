"""
CS3C, Assignment #4, lazy-delete binary tree
Ulises Marian
"""

from bst import *
import math

class LazyBinaryTreeNode(BinaryTreeNode):
    def __init__(self, *args):
        super().__init__(*args)
        self.deleted = False

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        #True if node is deleted
        #False otherwise
        self._deleted = deleted

    def __str__(self):
        s = super().__str__()
        if self.deleted:
            s = "(D)"
        return s

    def __repr__(self):
        return super().__repr__() + f" deleted: {self.deleted}"


class LazyBinarySearchTree(BinarySearchTree):
    TreeNode = LazyBinaryTreeNode

    def __init__(self):
        super().__init__(self)
        self._size_physical = 0

    @property
    def size_physical(self):
        return self._size_physical

    def __repr__(self):
        return f"physical size={self.size_physical}" + self._str(self._root,
                                                                 0, True)


    def _str(self, subtree_root, depth, _repr=False):
        if subtree_root is None:
            return ""

        s = ""
        s += self._str(subtree_root.right_child, depth + 1, _repr)
        s += (" " * 4 * depth
              + (repr(subtree_root) if _repr else str(subtree_root))
              + "\n")
        s += self._str(subtree_root.left_child, depth + 1, _repr)
        return s


    def _remove(self, subtree_root, data):
        if not subtree_root:
            raise BinarySearchTree.NotFoundError(f"data={data} not found")

        if data == subtree_root.data and subtree_root.deleted:
            raise BinarySearchTree.NotFoundError

        if data < subtree_root.data:
            subtree_root.left_child = self._remove(subtree_root.left_child,
                                                   data)
        elif subtree_root.data < data:
            subtree_root.right_child = self._remove(subtree_root.right_child,
                                                    data)
        else: #data == subtreet_root.data
            subtree_root.deleted = True
            self._size -= 1

        return subtree_root


    def __iter__(self, physical=False):

        if physical:
            gen = super().__iter__()
            for data in gen:
                yield data

        subtree_root = self._root
        if subtree_root is None:
            return

        #if subtree_root.deleted:
        try:
            if subtree_root.left_child.deleted:
                yield from self.__iter__(subtree_root.left_child)
        except:
            try:
                yield subtree_root.data
            except:
                yield from self.__iter__(subtree_root.right_child)

    def _insert(self, subtree_root, data):
        if subtree_root is None:
            self._size += 1
            self._size_physical += 1
            return self.TreeNode(data)

        if data == subtree_root.data and subtree_root.deleted:
            subtree_root.deleted = False
            self._size += 1
            return subtree_root
        if data == subtree_root.data:
            raise BinarySearchTree.DuplicateDataError(f"data={data} already exists in tree")
        elif data < subtree_root.data:
            subtree_root.left_child = self._insert(subtree_root.left_child, data)
        else:
            subtree_root.right_child = self._insert(subtree_root.right_child, data)

        return subtree_root

    def _find_node_recursive(self, subtree_root, data):
        if subtree_root is None:
            raise BinarySearchTree.NotFoundError

        if subtree_root.deleted:
            raise BinarySearchTree.NotFoundError

        if subtree_root.data == data:
            return subtree_root
        elif data < subtree_root.data:
            return self._find_node_recursive(subtree_root.left_child, data)
        else:
            return self._find_node_recursive(subtree_root.right_child, data)

    def find_min(self):
        return self._find_min_check()

    def _find_min_check(self):
        data = self._find_min(self._root)
        if data == math.inf:
            raise BinarySearchTree.EmptyTreeError
        return data

    def _find_min(self, subtree_root):
        if subtree_root is None:
            raise BinarySearchTree.EmptyTreeError

        try:
            if subtree_root.deleted:
                if subtree_root.left_child is not None:
                    left_result = min(math.inf, self._find_min(
                        subtree_root.left_child))
                    try:
                        right_result = min(math.inf, self._find_min(
                            subtree_root.right_child))
                        return min(left_result, right_result)
                    except:
                        right_result = math.inf
                        return min(left_result, right_result)
                else:
                    right_result = min(math.inf, self._find_min(
                        subtree_root.right_child))
                    return right_result
            else:
                result = min(subtree_root.data, self._find_min(
                subtree_root.left_child))
                return result
        except BinarySearchTree.EmptyTreeError:
            if subtree_root.deleted:
                return math.inf
            else:
                return subtree_root.data

    def find_max(self):
        return self._find_max_check()

    def _find_max_check(self):
        data = self._find_max(self._root)
        if data == -math.inf:
            raise BinarySearchTree.EmptyTreeError
        return data

    def _find_max(self, subtree_root):
        if subtree_root is None:
            raise BinarySearchTree.EmptyTreeError

        try:
            if subtree_root.deleted:
                if subtree_root.right_child is not None:
                    right_result = max(-math.inf, self._find_max(
                        subtree_root.right_child))
                    try:
                        left_result = max(-math.inf, self._find_max(
                            subtree_root.left_child))
                        return max(left_result, right_result)
                    except:
                        left_result = -math.inf
                        return max(left_result, right_result)
                else:
                    left_result = max(-math.inf, self._find_max(
                        subtree_root.left_child))
                    return left_result
            else:
                result = max(subtree_root.data, self._find_max(
                subtree_root.right_child))
                return result
        except BinarySearchTree.EmptyTreeError:
            if subtree_root.deleted:
                return -math.inf
            else:
                return subtree_root.data

    def garbage_collection_helper(self, tree_node):
        if tree_node is None:
            return
        tree_node.left_child = self.garbage_collection_helper(
            tree_node.left_child)
        tree_node.right_child = self.garbage_collection_helper(
            tree_node.right_child)
        if tree_node.deleted:
            tree_node = tree_node.left_child if tree_node.left_child \
                else tree_node.right_child

        return tree_node

    def collect_garbage(self):
        self._root = self.garbage_collection_helper(self._root)



def main():
    pass
