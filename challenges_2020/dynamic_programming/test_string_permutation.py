
import unittest

from string_permutation import check_inclusion


class StringPermutationTests(unittest.TestCase):
    """Tests for string permutation challenge."""

    def test_case_1(self):
        self.assertTrue(check_inclusion("ab", "eidbaooo"))

    def test_case_2(self):
        self.assertFalse(check_inclusion("ab", "eidboaoo"))

    def test_case_3(self):
        self.assertFalse(check_inclusion("hello", "ooolleoooleh"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
