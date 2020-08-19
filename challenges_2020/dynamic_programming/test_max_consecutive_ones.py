
import unittest

from max_consecutive_ones import find_max_consecutive_ones


class MaxConsecutiveOnesTests(unittest.TestCase):

    """Tests for max consecutive ones challenge."""

    def test_case_1(self):
        self.assertEqual(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
