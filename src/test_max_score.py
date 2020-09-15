
import unittest

from max_score import max_score


class MaxScoreTests(unittest.TestCase):

    """Tests for max_score challenge."""

    def test_case_1(self):
        self.assertEqual(max_score([1, 2, 3, 4, 5, 6, 1], k=3), 12)

    def test_case_2(self):
        self.assertEqual(max_score([2, 2, 2], k=2), 4)

    def test_case_3(self):
        self.assertEqual(max_score([9, 7, 7, 9, 7, 7, 9], k=7), 55)

    def test_case_4(self):
        self.assertEqual(max_score([1, 1000, 1], k=1), 1)

    def test_case_5(self):
        self.assertEqual(max_score([1, 79, 80, 1, 1, 1, 200, 1], k=3), 202)

    def test_case_6(self):
        self.assertEqual(max_score([2, 3, 4, 5, 12, 1, 1, 1], k=4), 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
