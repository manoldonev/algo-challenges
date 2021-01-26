
import unittest

from four_sum_ii import count_four_sum


class FourSumIiTests(unittest.TestCase):

    """Tests for four sum ii challenge."""

    def test_case_1(self):
        self.assertEqual(count_four_sum([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)

    def test_case_2(self):
        self.assertEqual(count_four_sum(
            [0, 1, -1], [-1, 1, 0], [0, 0, 1], [-1, 1, 1]), 17)

    def test_case_3(self):
        self.assertEqual(count_four_sum(
            [-1, -1], [-1, 1], [-1, 1], [1, -1]), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
