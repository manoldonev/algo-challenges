
import unittest

from sliding_window_median import median_sliding_window


class SlidingWindowMedianTests(unittest.TestCase):
    """Tests for sliding window maximum challenge."""

    def test_case_1(self):
        self.assertEqual(median_sliding_window(
            [1, 3, -1, -3, 5, 3, 6, 7], k=3), [1, -1, -1, 3, 5, 6])

    def test_case_2(self):
        self.assertEqual(median_sliding_window([1], k=1), [1])

    def test_case_3(self):
        self.assertEqual(median_sliding_window([1, -1], k=2), [0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
