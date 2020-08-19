
import unittest

from max_consecutive_ones_iii import find_max_consecutive_ones


class MaxConsecutiveOnesIiiTests(unittest.TestCase):

    """Tests for max consecutive ones iii challenge."""

    def test_case_1(self):
        self.assertEqual(find_max_consecutive_ones(
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)

    def test_case_2(self):
        self.assertEqual(find_max_consecutive_ones(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
