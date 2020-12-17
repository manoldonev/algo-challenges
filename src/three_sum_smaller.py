
"""3Sum Smaller"""

from typing import List


def find_three_sum_count(numbers: List[int], target: int) -> int:
    """https://leetcode.com/problems/3sum-smaller/"""

    result = 0
    numbers.sort()
    target_sentinel = target // 3
    for pivot_index, pivot in enumerate(numbers):
        if pivot > target_sentinel:
            break

        result += _calculate_triplet_count(numbers,
                                           pivot_index, target - pivot)

    return result


def _calculate_triplet_count(numbers: List[int], pivot_index: int, target: int) -> int:
    triplet_count = 0
    left = pivot_index + 1
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] >= target:
            right -= 1
        else:
            triplet_count += right - left
            left += 1

    return triplet_count
