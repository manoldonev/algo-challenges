
import unittest

from minimum_window_subsequence import minimum_window_subsequence


class MinimumWindowSubsequenceTests(unittest.TestCase):
    """Tests for minimum window subsequence challenge."""

    def test_case_1(self):
        self.assertTrue(minimum_window_subsequence("abcdebdde", "bde"), "bcde")


if __name__ == "__main__":
    unittest.main(verbosity=2)
