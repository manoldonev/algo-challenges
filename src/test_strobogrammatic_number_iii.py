
import unittest

from strobogrammatic_number_iii import find_strobogrammatic_in_range


class StrobogrammaticNumberIiiTests(unittest.TestCase):
    """Tests for strobogrammatic number iii challenge"""

    def test_case_1(self):
        self.assertEqual(find_strobogrammatic_in_range("50", "100"), 3)

    def test_case_2(self):
        self.assertEqual(find_strobogrammatic_in_range("100", "50"), 0)

    def test_case_3(self):
        self.assertEqual(find_strobogrammatic_in_range("0", "100"), 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
