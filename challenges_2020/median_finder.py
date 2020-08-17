
"""Find Median from Data Stream"""

import heapq


class MedianFinder:
    """https://leetcode.com/problems/find-median-from-data-stream/"""

    def __init__(self):
        self.max_heap_low = []
        self.min_heap_high = []

    def add_number(self, number: int) -> None:
        heapq.heappush(self.max_heap_low, -number)
        heapq.heappush(self.min_heap_high, -heapq.heappop(self.max_heap_low))

        if len(self.max_heap_low) < len(self.min_heap_high):
            heapq.heappush(self.max_heap_low, -
                           heapq.heappop(self.min_heap_high))

    def find_median(self) -> float:
        if len(self.max_heap_low) > len(self.min_heap_high):
            return -self.max_heap_low[0]
        else:
            return (-self.max_heap_low[0] + self.min_heap_high[0]) / 2
