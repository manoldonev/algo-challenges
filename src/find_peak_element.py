
"""Find Peak Element"""

from typing import List


def find_peak_element(numbers: List[int]) -> int:
    """https://leetcode.com/problems/find-peak-element/"""

    left = 0
    right = len(numbers) - 1

    while left < right:
        middle = (left + right) // 2
        if numbers[middle] > numbers[middle + 1]:
            right = middle
        else:
            left = middle + 1

    return left
