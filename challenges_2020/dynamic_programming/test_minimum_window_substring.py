
import unittest

from minimum_window_substring import minimum_window_substring


class MinimumWindowSubstringTests(unittest.TestCase):

    """Tests for minimum window substring challenge."""

    def test_case_1(self):
        self.assertEqual(minimum_window_substring(
            "ADOBECODEBANC", "ABC"), "BANC")

    def test_case_2(self):
        self.assertEqual(minimum_window_substring("a", "aa"), "")

    def test_case_3(self):
        self.assertEqual(minimum_window_substring("aa", "aa"), "aa")


if __name__ == "__main__":
    unittest.main(verbosity=2)
