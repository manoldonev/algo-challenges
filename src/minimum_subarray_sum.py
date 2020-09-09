
""" Minimum Size Subarray Sum"""

import sys

from typing import List


def minimum_subarray_sum(target: int, numbers: List[int]) -> int:
    """https://leetcode.com/problems/minimum-size-subarray-sum"""

    fast, slow = 0, 0
    current_sum = 0
    min_length = sys.maxsize

    for index, value in enumerate(numbers):
        fast = index
        current_sum += value

        while current_sum >= target:
            min_length = min(min_length, fast - slow + 1)
            current_sum -= numbers[slow]
            slow += 1

    return min_length if min_length != sys.maxsize else 0
