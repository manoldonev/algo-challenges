
"""Sliding Window Maximum"""

from collections import deque
from typing import List


def maximum_sliding_window(numbers: List[int], k: int) -> List[int]:
    """https://leetcode.com/problems/sliding-window-maximum/"""

    max_queue = deque([])
    max_sliding_window = []
    for index, value in enumerate(numbers):
        # maintain monotonous decreasing queue invariant
        while max_queue and max_queue[-1] < value:
            max_queue.pop()

        max_queue.append(value)

        if index < k - 1:
            continue

        max_sliding_window.append(max_queue[0])
        if max_queue[0] == numbers[index - k + 1]:
            max_queue.popleft()

    return max_sliding_window
