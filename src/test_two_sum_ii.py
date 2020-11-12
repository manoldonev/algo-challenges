
import unittest

from two_sum_ii import find_two_sum


class TwoSumTests(unittest.TestCase):

    """Tests for two sum challenge."""

    def test_case_1(self):
        self.assertEqual(find_two_sum([2, 7, 11, 15], 9), [1, 2])

    def test_case_2(self):
        self.assertEqual(find_two_sum([2, 3, 4], 6), [1, 3])

    def test_case_3(self):
        self.assertEqual(find_two_sum([3, 3], 6), [1, 2])

    def test_case_4(self):
        self.assertEqual(find_two_sum([-1, 0], -1), [1, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
