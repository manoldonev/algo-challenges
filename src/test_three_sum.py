
import unittest

from three_sum import find_three_sum


class ThreeSumTests(unittest.TestCase):

    """Tests for three sum challenge."""

    def test_case_1(self):
        self.assertEqual(find_three_sum(
            [-1, 0, 1, 2, -1, -4]), [[-1, 1, 0], [-1, 2, -1]])

    def test_case_2(self):
        self.assertEqual(find_three_sum([]), [])

    def test_case_3(self):
        self.assertEqual(find_three_sum([0]), [])

    def test_case_4(self):
        self.assertEqual(find_three_sum([0, 0, 0, 0]), [[0, 0, 0]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
