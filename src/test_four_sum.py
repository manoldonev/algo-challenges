
import unittest

from four_sum import find_four_sum


class FourSumTests(unittest.TestCase):

    """Tests for four sum challenge."""

    def test_case_1(self):
        self.assertEqual(find_four_sum(
            [1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    def test_case_2(self):
        self.assertEqual(find_four_sum(
            [-2, -1, -1, 1, 1, 2, 2], 0), [[-2, -1, 1, 2], [-1, -1, 1, 1]])

    def test_case_3(self):
        self.assertEqual(find_four_sum(
            [-1, -5, -5, -3, 2, 5, 0, 4], -7), [[-5, -5, -1, 4], [-5, -3, -1, 2]])

    def test_case_4(self):
        self.assertEqual(find_four_sum(
            [-1, 0, 1, 2, -1, -4], -1), [[-4, 0, 1, 2], [-1, -1, 0, 1]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
