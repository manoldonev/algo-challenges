
"""3Sum Closest"""

import sys

from typing import List


def find_three_sum_closest(numbers: List[int], target: int) -> int:
    """https://leetcode.com/problems/3sum-closest/"""

    numbers.sort()

    last_index = len(numbers) - 1
    min_diff = sys.maxsize

    for pivot_index, pivot in enumerate(numbers):
        left = pivot_index + 1
        right = last_index
        if left == right or min_diff == 0:
            break

        while left < right:
            current_diff = target - pivot - numbers[left] - numbers[right]
            if abs(current_diff) < abs(min_diff):
                min_diff = current_diff

            if current_diff == 0:
                break

            if current_diff < 0:
                right -= 1
            else:
                left += 1

    return target - min_diff
