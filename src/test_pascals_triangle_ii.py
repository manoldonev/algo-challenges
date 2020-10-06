
import unittest

from pascals_triangle_ii import get_row


class PascalsTriangleIITests(unittest.TestCase):
    """Tests for Pascal's Triangle II challenge."""

    def test_case_1(self):
        self.assertEqual(get_row(3), [1, 3, 3, 1])

    def test_case_2(self):
        self.assertEqual(get_row(0), [1])

    def test_case_3(self):
        self.assertEqual(get_row(1), [1, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
