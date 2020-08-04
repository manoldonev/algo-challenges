
import unittest

from maximum_length_repeated_subarray import find_length


class MaximumLengthRepeatedSubarrayTests(unittest.TestCase):
    """Tests for maximim length repeated subarray challenge."""

    def test_case_1(self):
        self.assertEqual(find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
