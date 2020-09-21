
import unittest

from house_robber_ii import rob


class HouseRobberIITests(unittest.TestCase):
    """Tests for house robber ii challenge"""

    def test_case_1(self):
        self.assertEqual(rob([2, 3, 2]), 3)

    def test_case_2(self):
        self.assertEqual(rob([1]), 1)

    def test_case_3(self):
        self.assertEqual(rob([1, 2, 3, 1]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
