
import unittest

from wiggle_sort import wiggle_sort


class WiggleSortTests(unittest.TestCase):
    """Test cases for wiggle sort challenge"""

    def test_case_1(self):
        numbers = [3, 5, 2, 1, 6, 4]
        wiggle_sort(numbers)
        self.assertEqual(numbers, [3, 5, 1, 6, 2, 4])

    def test_case_2(self):
        numbers = [2, 1]
        wiggle_sort(numbers)
        self.assertEqual(numbers, [1, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
