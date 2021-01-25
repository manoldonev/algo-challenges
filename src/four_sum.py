
"""4Sum"""

from typing import List


def find_four_sum(numbers: List[int], target: int) -> List[List[int]]:
    """https://leetcode.com/problems/4sum/"""

    numbers.sort()
    n_sum = 4
    result = []
    find_n_sum(numbers, target, 0, len(numbers) - 1, n_sum, [], result)

    return result


def find_n_sum(numbers: List[int], target: int, left: int, right: int, n_sum: int, current: List[int], result: List[List[int]]):
    if right - left + 1 < n_sum or \
            target < numbers[left] * n_sum or target > numbers[right] * n_sum:
        return

    if n_sum == 2:
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                result.append(current + [numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1

                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif current_sum > target:
                right -= 1
            else:
                left += 1
    else:
        for i in range(left, right + 1):
            if i == left or numbers[i - 1] != numbers[i]:
                find_n_sum(
                    numbers, target - numbers[i], i + 1, right, n_sum - 1, current + [numbers[i]], result)
