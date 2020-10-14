
import unittest

from longest_consecutive_sequence import find_longest_consecutive_sequence


class LongestConsecutiveSequenceTests(unittest.TestCase):
    """Tests for longest consecutive sequence challenge."""

    def test_case_1(self):
        self.assertEqual(find_longest_consecutive_sequence(
            [100, 4, 200, 1, 3, 2]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
