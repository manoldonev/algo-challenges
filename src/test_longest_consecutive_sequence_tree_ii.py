
import unittest

from longest_consecutive_sequence_tree_ii import find_longest_consecutive_sequence, TreeNode


class LongestConsecutiveSequenceTreeTests(unittest.TestCase):
    """Tests for longest consecutive sequence binary tree II challenge."""

    def test_case_1(self):
        root = None
        self.assertEqual(find_longest_consecutive_sequence(root), 0)

    def test_case_2(self):
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3))
        self.assertEqual(find_longest_consecutive_sequence(root), 2)

    def test_case_3(self):
        root = TreeNode(2,
                        TreeNode(1),
                        TreeNode(3))
        self.assertEqual(find_longest_consecutive_sequence(root), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
