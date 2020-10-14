
import unittest

from longest_consecutive_sequence_tree import find_longest_consecutive_sequence, TreeNode


class LongestConsecutiveSequenceTreeTests(unittest.TestCase):
    """Tests for longest consecutive sequence binary tree challenge."""

    def test_case_1(self):
        root = None
        self.assertEqual(find_longest_consecutive_sequence(root), 0)

    def test_case_2(self):
        root = TreeNode(1,
                        None,
                        TreeNode(3,
                                 TreeNode(2),
                                 TreeNode(4,
                                          None,
                                          TreeNode(5))))
        self.assertEqual(find_longest_consecutive_sequence(root), 3)

    def test_case_3(self):
        root = TreeNode(2,
                        None,
                        TreeNode(3,
                                 TreeNode(2,
                                          TreeNode(1))))
        self.assertEqual(find_longest_consecutive_sequence(root), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
