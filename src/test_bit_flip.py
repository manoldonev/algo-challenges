
import unittest

from bit_flip import bit_flip


class BitFlipTests(unittest.TestCase):

    """Tests for bit flip challenge."""

    def test_case_1(self):
        self.assertEqual(bit_flip([0, 1, 0, 0, 1, 1, 0]), 6)

    def test_case_2(self):
        self.assertEqual(bit_flip([0, 0, 0, 0, 0, 0, 0]), 7)

    def test_case_3(self):
        self.assertEqual(bit_flip([1, 1, 1, 1, 1, 1, 1]), 7)

    def test_case_4(self):
        self.assertEqual(bit_flip([1, 0, 0, 0, 0, 0, 1]), 6)

    def test_case_5(self):
        self.assertEqual(bit_flip([1, 0, 0, 1, 0, 0, 1]), 5)

    def test_case_6(self):
        self.assertEqual(bit_flip([1, 0, 1, 0, 1, 0, 1]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
