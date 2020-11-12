
"""Two Sum II"""

from typing import List


def find_two_sum(numbers: List[int], target: int) -> List[int]:
    """https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

    left = 0
    right = len(numbers) - 1

    while True:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            break

    return [left + 1, right + 1]
