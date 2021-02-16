
"""Valid Mountain Array"""

from typing import List


def is_valid_mountain_array(numbers: List[int]) -> bool:
    """https://leetcode.com/problems/valid-mountain-array"""

    n = len(numbers)
    if n < 3:
        return False

    left = 0
    right = n - 1

    while left < n - 1 and numbers[left] < numbers[left + 1]:
        left += 1

    if left in (0, right):
        return False

    while left < right and numbers[left] > numbers[left + 1]:
        left += 1

    return left == right
