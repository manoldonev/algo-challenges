
import unittest

from sliding_window_k_maximum import maximum_sliding_window


class SlidingWindowKMaximumTests(unittest.TestCase):
    """Tests for sliding window maximum challenge."""

    def test_case_1(self):
        self.assertEqual(maximum_sliding_window(
            [1, 3, -1, -3, 5, 3, 6, 7], k=3), [3, 3, 5, 5, 6, 7])


if __name__ == "__main__":
    unittest.main(verbosity=2)
