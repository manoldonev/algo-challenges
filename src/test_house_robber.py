
import unittest

from house_robber import rob


class HouseRobberTests(unittest.TestCase):
    """Tests for house robber challenge"""

    def test_case_1(self):
        self.assertEqual(rob([1, 2, 3, 1]), 4)

    def test_case_2(self):
        self.assertEqual(rob([2, 1, 1, 2]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
