
import unittest

from longest_substring_at_most_k_distinct_characters import find_length


class LongestSubstringAtMostKDistinctCharacters(unittest.TestCase):
    """Tests for longest substring with at most k (default = 2) distinct characters challenge."""

    def test_case_two_distinct_characters_1(self):
        self.assertEqual(find_length("eceba"), 3)

    def test_case_two_distinct_characters_2(self):
        self.assertEqual(find_length("abbac"), 4)

    def test_case_two_distinct_characters_3(self):
        self.assertEqual(find_length("abbacaca"), 5)

    def test_case_two_distinct_characters_4(self):
        self.assertEqual(find_length("abbaba"), 6)

    def test_case_two_distinct_characters_5(self):
        self.assertEqual(find_length("aaaaaa"), 6)

    def test_case_two_distinct_characters_6(self):
        self.assertEqual(find_length("abbacdfghiababababad"), 9)

    def test_case_three_distinct_characters_1(self):
        self.assertEqual(find_length("abbacdfghiababababad", k=3), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
