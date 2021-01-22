
"""4Sum"""

from typing import List


def find_four_sum(numbers: List[int], target: int) -> List[List[int]]:
    """https://leetcode.com/problems/4sum/"""

    result = []
    numbers.sort()

    n = len(numbers)
    target_sentinel = target // 4
    target_sentinel2 = target // 2
    for pivot_index in range(n):
        pivot1 = numbers[pivot_index]
        if pivot1 > target_sentinel:
            break

        if pivot_index > 0 and \
                numbers[pivot_index - 1] == numbers[pivot_index]:
            continue

        for secondary_pivot_index in range(pivot_index + 1, n):
            pivot2 = numbers[secondary_pivot_index]
            if pivot1 + pivot2 > target_sentinel2:
                break

            if secondary_pivot_index == pivot_index + 1 or \
                    numbers[secondary_pivot_index - 1] != numbers[secondary_pivot_index]:
                remaining_target = target - pivot1 - pivot2
                for pair in _find_two_sum(numbers, secondary_pivot_index, remaining_target):
                    result.append([pivot1, pivot2, *pair])

    return result


def _find_two_sum(numbers: List[int], pivot_index: int, target: int) -> List[List[int]]:
    n = len(numbers)
    left = pivot_index + 1
    right = n - 1

    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            yield [numbers[left], numbers[right]]
            left += 1
            right -= 1
            while left < right and numbers[left] == numbers[left - 1]:
                left += 1

            while left < right and numbers[right] == numbers[right + 1]:
                right -= 1
        elif current > target:
            right -= 1
        else:
            left += 1
