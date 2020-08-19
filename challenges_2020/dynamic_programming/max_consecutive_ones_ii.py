
"""Max Consecutive Ones II"""

from typing import List


def find_max_consecutive_ones(numbers: List[int]) -> int:
    """https://leetcode.com/problems/max-consecutive-ones-ii/"""
    left = 0
    remaining_zeroes_to_flip = 1
    for right, value in enumerate(numbers):
        remaining_zeroes_to_flip -= 1 - value
        if remaining_zeroes_to_flip < 0:
            out_value = numbers[left]
            remaining_zeroes_to_flip += 1 - out_value
            left += 1

    if not numbers:
        return 0

    return right - left + 1
