""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

import sys


def check_binary_search_tree_(root):
    """https://www.hackerrank.com/challenges/ctci-is-binary-search-tree"""

    return _check_bst(root)


def _check_bst(root, min_value=-sys.maxint, max_value=sys.maxint):
    if not root:
        return True

    if root.data <= min_value or root.data >= max_value:
        return False

    return _check_bst(root.left, min_value, root.data) and \
        _check_bst(root.right, root.data, max_value)


# def check_binary_search_tree_(root):
#     previous_value = -sys.maxint
#     for node in _inorder(root):
#         if previous_value >= node.data:
#             return False

#         previous_value = node.data

#     return True


# def _inorder(root):
#     if not root:
#         return

#     for node in _inorder(root.left):
#         yield node

#     yield root

#     for node in _inorder(root.right):
#         yield node
