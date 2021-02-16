

import unittest

from minimum_mountain_removals import minimum_mountain_removals


class MinimumMountainRemovalsTests(unittest.TestCase):
    """Tests for minimum mountain removals challenge."""

    def test_case_1(self):
        self.assertEqual(minimum_mountain_removals([1, 3, 1]), 0)

    def test_case_2(self):
        self.assertEqual(minimum_mountain_removals(
            [2, 1, 1, 5, 6, 2, 3, 1]), 3)

    def test_case_3(self):
        self.assertEqual(minimum_mountain_removals([2, 1, 1, 5, 6, 3, 1]), 2)

    def test_case_4(self):
        self.assertEqual(minimum_mountain_removals(
            [4, 3, 2, 1, 1, 2, 3, 1]), 4)

    def test_case_5(self):
        self.assertEqual(minimum_mountain_removals(
            [1, 2, 3, 4, 4, 3, 2, 1]), 1)

    def test_case_6(self):
        self.assertEqual(minimum_mountain_removals(
            [9, 8, 1, 7, 6, 5, 4, 3, 2, 1]), 2)

    def test_case_7(self):
        self.assertEqual(minimum_mountain_removals(
            [1, 16, 84, 9, 29, 71, 86, 79, 72, 12]), 2)

    def test_case_8(self):
        self.assertEqual(minimum_mountain_removals(
            [10, 9, 8, 7, 6, 5, 4, 5, 4]), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
