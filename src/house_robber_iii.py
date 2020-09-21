
"""House Robber III"""

from typing import Tuple


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode) -> int:
    """https://leetcode.com/problems/house-robber/"""
    return max(_rob(root))


def _rob(node: TreeNode) -> Tuple:
    if not node:
        return (0, 0)

    left, right = _rob(node.left), _rob(node.right)
    rob_node = node.val + left[1] + right[1]
    skip_node = max(left) + max(right)

    return rob_node, skip_node
