
import unittest

from online_stock_span import StockSpanner


class OnlineStockSpanTests(unittest.TestCase):
    """Tests for online stock span challenge."""

    def test_case_1(self):
        spanner = StockSpanner()
        result = []
        for value in [100, 80, 60, 70, 60, 75, 85]:
            result.append(spanner.next(value))

        self.assertEqual(result, [1, 1, 1, 2, 1, 4, 6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
