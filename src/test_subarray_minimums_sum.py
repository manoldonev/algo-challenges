
import unittest

from subarray_minimums_sum import sum_subarray_minimums


class SubarrayMinimumsSumTests(unittest.TestCase):
    """Tests for subarray minimums sum challenge."""

    def test_case_1(self):
        self.assertTrue(sum_subarray_minimums([3, 1, 2, 4]), 17)

    def test_case_2(self):
        self.assertTrue(sum_subarray_minimums([2, 9, 7, 8, 3, 4, 6, 1]), 117)


if __name__ == "__main__":
    unittest.main(verbosity=2)
