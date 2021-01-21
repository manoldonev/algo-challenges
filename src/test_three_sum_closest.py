
import unittest

from three_sum_closest import find_three_sum_closest


class ThreeSumClosestTests(unittest.TestCase):
    """Tests for three sum closest challenge."""

    def test_case_1(self):
        self.assertEqual(find_three_sum_closest([-1, 2, 1, -4], 1), 2)

    def test_case_2(self):
        self.assertEqual(find_three_sum_closest([0, 0, 0], 1), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
