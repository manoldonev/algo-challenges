
import unittest

from three_sum_smaller import find_three_sum_count


class ThreeSumSmallerTests(unittest.TestCase):
    """Tests for three sum smaller challenge."""

    def test_case_1(self):
        self.assertEqual(find_three_sum_count([-2, 0, 1, 3], 2), 2)

    def test_case_2(self):
        self.assertEqual(find_three_sum_count([3, 1, 0, -2], 4), 3)

    def test_case_3(self):
        self.assertEqual(find_three_sum_count([0, 0, 0], 0), 0)

    def test_case_4(self):
        self.assertEqual(find_three_sum_count([1, 0, -1], 0), 0)

    def test_case_5(self):
        self.assertEqual(find_three_sum_count([1, 1, -2], 1), 1)

    def test_case_6(self):
        self.assertEqual(find_three_sum_count([0, -4, -1, 1, -1, 2], -5), 1)

    def test_case_7(self):
        self.assertEqual(find_three_sum_count(
            [3, 2, -2, 6, 2, -2, 6, -2, -4, 2, 3, 0, 4, 4, 1], 3), 151)


if __name__ == "__main__":
    unittest.main(verbosity=2)
