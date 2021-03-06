
"""4Sum"""

from typing import List


def find_four_sum(numbers: List[int], target: int) -> List[List[int]]:
    """https://leetcode.com/problems/4sum/"""

    numbers.sort()
    k_sum = 4
    result = []
    find_k_sum(numbers, target, 0, len(numbers) - 1, k_sum, [], result)

    return result


def find_k_sum(numbers: List[int], target: int, left: int, right: int, k_sum: int, current: List[int], result: List[List[int]]):
    if right - left + 1 < k_sum or \
            target < numbers[left] * k_sum or target > numbers[right] * k_sum:
        return

    if k_sum == 2:
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
                find_k_sum(
                    numbers, target - numbers[i], i + 1, right, k_sum - 1, current + [numbers[i]], result)
