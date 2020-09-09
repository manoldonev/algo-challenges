
import unittest

from lis_length import find_length_of_lis


class LISLengthTests(unittest.TestCase):

    """Tests for length of longest increasing subsequence challenge."""

    def test_case_1(self):
        self.assertEqual(find_length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_case_2(self):
        self.assertEqual(find_length_of_lis([]), 0)

    def test_case_3(self):
        self.assertEqual(find_length_of_lis([0]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
