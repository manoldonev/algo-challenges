
import unittest

from find_peak_element import find_peak_element


class FindPeakElementTests(unittest.TestCase):
    """Tests for find peak element tests"""

    def test_case_1(self):
        self.assertEqual(find_peak_element([1, 2, 3, 1]), 2)

    def test_case_2(self):
        self.assertEqual(find_peak_element([1]), 0)

    def test_case_3(self):
        self.assertEqual(find_peak_element([1, 2, 3, 4]), 3)

    def test_case_4(self):
        self.assertEqual(find_peak_element([4, 3, 2, 1]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
