
"""Binary Tree Longest Consecutive Sequence II"""

from typing import Tuple


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_longest_consecutive_sequence(root: TreeNode) -> int:
    """https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/"""

    def find_longest_path(root: TreeNode) -> Tuple:
        if not root:
            return 0, 0, 0

        increasing = decreasing = 1
        max_left = max_right = 0
        if root.left:
            left_increasing, left_decreasing, max_left = find_longest_path(
                root.left)
            if root.val == root.left.val - 1:
                increasing = left_increasing + 1
            elif root.val == root.left.val + 1:
                decreasing = left_decreasing + 1

        if root.right:
            right_increasing, right_decreasing, max_right = find_longest_path(
                root.right)
            if root.val == root.right.val - 1:
                increasing = max(increasing, right_increasing + 1)
            elif root.val == root.right.val + 1:
                decreasing = max(decreasing, right_decreasing + 1)

        max_length = max(max_left, max_right, decreasing + increasing - 1)

        return increasing, decreasing, max_length

    return find_longest_path(root)[2]
