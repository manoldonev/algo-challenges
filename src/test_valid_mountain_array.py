
import unittest

from valid_mountain_array import is_valid_mountain_array


class ValidMountainArrayTests(unittest.TestCase):
    """Tests for valid mountain array challenge."""

    def test_case_1(self):
        self.assertFalse(is_valid_mountain_array(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_case_2(self):
        self.assertTrue(is_valid_mountain_array(
            [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 11]))

    def test_case_3(self):
        self.assertFalse(is_valid_mountain_array([2, 1]))

    def test_case_4(self):
        self.assertFalse(is_valid_mountain_array([3, 5, 5]))

    def test_case_5(self):
        self.assertTrue(is_valid_mountain_array([0, 3, 2, 1]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
