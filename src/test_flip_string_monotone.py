
import unittest

from flip_string_monotone import count_min_flips


class MinFlipStringMonotoneIncreasingTests(unittest.TestCase):
    """Tests for flip string to monotone increasing challenge"""

    def test_case_1(self):
        self.assertEqual(count_min_flips('00110'), 1)

    def test_case_2(self):
        self.assertEqual(count_min_flips('010110'), 2)

    def test_case_2(self):
        self.assertEqual(count_min_flips('00011000'), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
