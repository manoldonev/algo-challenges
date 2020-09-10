
import unittest

from pattern_132 import find_132_pattern


class Pattern132Tests(unittest.TestCase):

    """Tests for pattern 132 challenge."""

    def test_case_1(self):
        self.assertFalse(find_132_pattern([1, 2, 3, 4]))

    def test_case_2(self):
        self.assertTrue(find_132_pattern([3, 1, 4, 2]))

    def test_case_3(self):
        self.assertTrue(find_132_pattern([-1, 3, 2, 0]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
