
import unittest

from contains_duplicate import contains_duplicate


class ContainsDuplicate(unittest.TestCase):
    """Tests for contains duplicate challenge"""

    def test_case_1(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))

    def test_case_2(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_case_3(self):
        self.assertTrue(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
