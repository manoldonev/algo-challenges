
import unittest

from strobogrammatic_number import is_strobogrammatic


class StrobogrammaticNumberTests(unittest.TestCase):
    """Tests for strobogrammatic number challenge"""

    def test_case_1(self):
        self.assertTrue(is_strobogrammatic('69'))

    def test_case_2(self):
        self.assertTrue(is_strobogrammatic('88'))

    def test_case_3(self):
        self.assertFalse(is_strobogrammatic('962'))

    def test_case_4(self):
        self.assertTrue(is_strobogrammatic('1'))

    def test_case_5(self):
        self.assertFalse(is_strobogrammatic('69569'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
