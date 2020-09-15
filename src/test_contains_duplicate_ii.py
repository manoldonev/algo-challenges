
import unittest

from contains_duplicate_ii import contains_nearby_duplicate


class ContainsDuplicateIITests(unittest.TestCase):
    """Tests for contains duplicate II challenge"""

    def test_case_1(self):
        self.assertTrue(contains_nearby_duplicate([1, 2, 3, 1], k=3))

    def test_case_2(self):
        self.assertTrue(contains_nearby_duplicate([1, 0, 1, 1], k=1))

    def test_case_3(self):
        self.assertFalse(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], k=2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
