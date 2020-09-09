
import unittest

from lis_count import find_number_of_lis


class LISCountTests(unittest.TestCase):

    """Tests for number of longest increasing subsequences challenge."""

    def test_case_1(self):
        self.assertEqual(find_number_of_lis([1, 3, 5, 4, 7]), 2)

    def test_case_2(self):
        self.assertEqual(find_number_of_lis([]), 0)

    def test_case_3(self):
        self.assertEqual(find_number_of_lis([0]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
