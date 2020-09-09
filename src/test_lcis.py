
import unittest

from lcis import find_lcis_length


class LCISTests(unittest.TestCase):
    """Tests for longest continuous increasing subsequence challenge."""

    def test_case_1(self):
        self.assertEqual(find_lcis_length([1, 3, 5, 4, 7]), 3)

    def test_case_2(self):
        self.assertEqual(find_lcis_length([2, 2, 2, 2, 2]), 1)

    def test_case_3(self):
        self.assertEqual(find_lcis_length([1, 3, 5, 7]), 4)

    def test_case_4(self):
        self.assertEqual(find_lcis_length([1, 3, 5, 4, 2, 3, 4, 5]), 4)

    def test_case_5(self):
        self.assertEqual(find_lcis_length([2, 1, 3]), 2)

    def test_case_6(self):
        self.assertEqual(find_lcis_length([-1, -3, -5, -4, -7]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
