
"""Binary Tree Longest Consecutive Sequence"""


class TreeNode:
    """Implementation of a tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_longest_consecutive_sequence(root: TreeNode) -> int:
    """https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/"""

    max_length = 0
    if root is None:
        return max_length

    stack = [(root, 1)]
    while stack:
        node, current_length = stack.pop()
        if node.right:
            stack.append((node.right,
                          current_length + 1
                          if node.right.val == node.val + 1
                          else 1))

        if node.left:
            stack.append((node.left,
                          current_length + 1
                          if node.left.val == node.val + 1
                          else 1))

        max_length = max(max_length, current_length)

    return max_length
