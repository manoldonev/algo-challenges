
"""Wiggle Sort"""

from typing import List


def wiggle_sort(numbers: List[int]) -> None:
    """https://leetcode.com/problems/wiggle-sort"""

    n = len(numbers)
    for i in range(1, n, 2):
        if numbers[i] < numbers[i - 1]:
            numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]

        if i + 1 < n and numbers[i] < numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
