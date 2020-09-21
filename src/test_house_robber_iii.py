
import unittest

from house_robber_iii import rob, TreeNode


class HouseRobberIIITests(unittest.TestCase):
    """Tests for house robber iii challenge"""

    def test_case_1(self):
        root = TreeNode(3,
                        TreeNode(2,
                                 None,
                                 TreeNode(3)),
                        TreeNode(3,
                                 None,
                                 TreeNode(1)))
        self.assertEqual(rob(root), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
