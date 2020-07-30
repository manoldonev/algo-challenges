
import unittest

from minimum_subarray_sum import minimum_subarray_sum


class MinimumSubarraySumTests(unittest.TestCase):
    """Tests for minimum subarray sum challenge."""

    def test_case_1(self):
        self.assertEqual(minimum_subarray_sum(7, [2, 3, 1, 2, 4, 3]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
