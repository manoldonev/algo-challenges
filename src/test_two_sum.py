
import unittest

from two_sum import find_two_sum


class TwoSumTests(unittest.TestCase):

    """Tests for two sum challenge."""

    def test_case_1(self):
        self.assertEqual(find_two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_case_2(self):
        self.assertEqual(find_two_sum([3, 2, 4], 6), [1, 2])

    def test_case_3(self):
        self.assertEqual(find_two_sum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
