
"""Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit"""

from typing import List
from collections import deque


def longest_subarray(numbers: List[int], limit: int) -> int:
    """https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/"""

    # monotone increasing queue with indices that could become the sliding window minimum
    min_queue = deque()

    # monotone decreasing queue with indices that could become the sliding window maximum
    max_queue = deque()

    left, max_length = 0, 0

    for right, value in enumerate(numbers):
        # maintain monotone queue invariants
        while min_queue and numbers[min_queue[-1]] > value:
            min_queue.pop()

        min_queue.append(right)

        while max_queue and numbers[max_queue[-1]] < value:
            max_queue.pop()

        max_queue.append(right)

        while numbers[max_queue[0]] - numbers[min_queue[0]] > limit:
            if max_queue[0] < min_queue[0]:
                left = max_queue.popleft() + 1
            else:
                left = min_queue.popleft() + 1

        max_length = max(max_length, right - left + 1)

    return max_length


def longest_subarray_bidirectional_pointer(numbers: List[int], limit: int) -> int:
    if not numbers:
        return 0

    min_value = max_value = numbers[0]
    max_length = 0
    left, start = 0, 0
    for right, value in enumerate(numbers):
        if value < min_value:
            min_value = value

        if value > max_value:
            max_value = value

        # if invalid, turn to count right-to-left
        if max_value - min_value > limit:
            min_value = max_value = value
            left = right
            while left - 1 >= start and \
                    abs(max_value - numbers[left - 1]) <= limit and \
                    abs(min_value - numbers[left - 1]) <= limit:
                left -= 1
                if numbers[left] < min_value:
                    min_value = numbers[left]

                if numbers[left] > max_value:
                    max_value = numbers[left]

            start = right

        max_length = max(max_length, right - left + 1)

    return max_length
