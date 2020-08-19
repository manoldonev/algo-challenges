
"""Max Consecutive Ones"""

from typing import List


def find_max_consecutive_ones(numbers: List[int]) -> int:
    """https://leetcode.com/problems/max-consecutive-ones/"""

    current_sum, max_sum = 0, 0
    for value in numbers:
        current_sum += value
        if not value:
            max_sum = max(max_sum, current_sum)
            current_sum = 0

    return max(max_sum, current_sum)
