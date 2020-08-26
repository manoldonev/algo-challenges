
import unittest

from move_zeroes import move_zeroes


class MoveZeroesTests(unittest.TestCase):
    """Tests for move zeroes challenge."""

    def test_case_1(self):
        numbers = [0, 1, 0, 3, 12]
        move_zeroes(numbers)
        self.assertEqual(numbers, [1, 3, 12, 0, 0])

    def test_case_2(self):
        numbers = [0, 0, 0, 0, 0]
        move_zeroes(numbers)
        self.assertEqual(numbers, [0, 0, 0, 0, 0])

    def test_case_3(self):
        numbers = [1, 2, 3, 4, 5]
        move_zeroes(numbers)
        self.assertEqual(numbers, [1, 2, 3, 4, 5])

    def test_case_4(self):
        numbers = [1, 0, 0, 0, 0]
        move_zeroes(numbers)
        self.assertEqual(numbers, [1, 0, 0, 0, 0])

    def test_case_5(self):
        numbers = [0, 0, 0, 0, 1]
        move_zeroes(numbers)
        self.assertEqual(numbers, [1, 0, 0, 0, 0])

    def test_case_6(self):
        numbers = [0, 1, 0, 2, 0]
        move_zeroes(numbers)
        self.assertEqual(numbers, [1, 2, 0, 0, 0])

    def test_case_7(self):
        numbers = [1, 0, 2, 0, 3]
        move_zeroes(numbers)
        self.assertEqual(numbers, [1, 2, 3, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
