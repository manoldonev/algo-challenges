
"""Minimum Number of Removals to Make Mountain Array"""

from typing import List


def minimum_mountain_removals(numbers: List[int]) -> int:
    """https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array"""

    n = len(numbers)
    if n < 3:
        return 0

    # max increasing subarray ending at position i (left to right)
    max_increasing = [0] * n

    # max decreasing subarray ending at position i (right to left)
    max_decreasing = [0] * n

    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                max_increasing[i] = max(
                    max_increasing[i], max_increasing[j] + 1)

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if numbers[i] > numbers[j]:
                max_decreasing[i] = max(
                    max_decreasing[i], max_decreasing[j] + 1)

    max_mountain_length = 0
    for i in range(n):
        if max_increasing[i] > 0 and max_decreasing[i] > 0:
            max_mountain_length = max(
                max_mountain_length, max_increasing[i] + max_decreasing[i])

    return n - max_mountain_length - 1
