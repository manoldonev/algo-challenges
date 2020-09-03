
import unittest

from daily_temperatures import daily_temperatures


class DailyTemperaturesTests(unittest.TestCase):
    """Tests for daily temperatures challenge."""

    def test_case_1(self):
        self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
                         [1, 1, 4, 2, 1, 1, 0, 0])

    def test_case_2(self):
        self.assertEqual(daily_temperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]),
                         [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
