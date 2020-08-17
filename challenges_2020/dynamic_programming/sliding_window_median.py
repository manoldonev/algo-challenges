
"""Sliding Window Median"""

import heapq

from typing import List
from collections import Counter


def median_sliding_window(numbers: List[int], k: int) -> List[float]:
    """https://leetcode.com/problems/sliding-window-median"""

    medians = []
    max_heap_low = []
    min_heap_high = []
    invalid_numbers = Counter()
    is_window_odd = k % 2

    for i in range(k):
        heapq.heappush(max_heap_low, -numbers[i])

    for _ in range(k // 2):
        heapq.heappush(min_heap_high, -heapq.heappop(max_heap_low))

    n = len(numbers)
    i = k
    while True:
        if is_window_odd:
            medians.append(-max_heap_low[0])
        else:
            medians.append((-max_heap_low[0] + min_heap_high[0]) / 2)

        if i >= n:
            break

        out_number = numbers[i - k]
        in_number = numbers[i]
        i += 1

        invalid_numbers[out_number] += 1

        balance = 0
        if out_number <= -max_heap_low[0]:
            balance -= 1
        else:
            balance += 1

        if max_heap_low and in_number <= -max_heap_low[0]:
            balance += 1
            heapq.heappush(max_heap_low, -in_number)
        else:
            balance -= 1
            heapq.heappush(min_heap_high, in_number)

        # rebalance heaps
        if balance < 0:
            heapq.heappush(max_heap_low, -heapq.heappop(min_heap_high))
            balance += 1
        elif balance > 0:
            heapq.heappush(min_heap_high, -heapq.heappop(max_heap_low))
            balance -= 1

        # remove invalid numbers from heap tops
        while max_heap_low and invalid_numbers[-max_heap_low[0]]:
            invalid_numbers[-max_heap_low[0]] -= 1
            heapq.heappop(max_heap_low)

        while min_heap_high and invalid_numbers[min_heap_high[0]]:
            invalid_numbers[min_heap_high[0]] -= 1
            heapq.heappop(min_heap_high)

    return medians


if __name__ == "__main__":
    print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(median_sliding_window([1], k=1))
