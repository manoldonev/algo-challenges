
"""Online Stock Span"""


class StockSpanner:
    """https://leetcode.com/problems/online-stock-span/"""

    def __init__(self):
        # monotone decreasing stack
        self.min_stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.min_stack and self.min_stack[-1][0] <= price:
            weight += self.min_stack.pop()[1]

        self.min_stack.append((price, weight))

        return weight


if __name__ == "__main__":
    spanner = StockSpanner()
    for value in [100, 80, 60, 70, 60, 75, 85]:
        print(spanner.next(value))
