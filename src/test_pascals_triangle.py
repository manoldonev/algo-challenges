
import unittest

from pascals_triangle import generate


class PascalsTriangleTests(unittest.TestCase):
    """Tests for Pascal's Triangle challenge."""

    def test_case_1(self):
        self.assertEqual(generate(5), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ])

    def test_case_2(self):
        self.assertEqual(generate(0), [])

    def test_case_3(self):
        self.assertEqual(generate(1), [[1]])

    def test_case_4(self):
        self.assertEqual(generate(2), [[1], [1, 1]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
