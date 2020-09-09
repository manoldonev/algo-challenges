
import unittest

from max_consecutive_ones_ii import find_max_consecutive_ones


class MaxConsecutiveOnesIiTests(unittest.TestCase):

    """Tests for max consecutive ones ii challenge."""

    def test_case_1(self):
        self.assertEqual(find_max_consecutive_ones([1, 0, 1, 1, 0]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
