
import unittest

from longest_distinct_substring import find_length


class LongestDistinctSubstringLengthTests(unittest.TestCase):
    """Tests for longest substring with no repeated characters challenge."""

    def test_case_1(self):
        self.assertEqual(find_length("abcabcbb"), 3)

    def test_case_2(self):
        self.assertEqual(find_length("abba"), 2)

    def test_case_3(self):
        self.assertEqual(find_length("bbb"), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
