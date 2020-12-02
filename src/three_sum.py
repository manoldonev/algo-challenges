
"""3Sum"""

from typing import List


def find_three_sum(numbers: List[int]) -> List[List[int]]:
    """https://leetcode.com/problems/3sum/"""

    result = []
    numbers.sort()
    for pivot_index, pivot in enumerate(numbers):
        if pivot > 0:
            break

        if pivot_index == 0 or \
                numbers[pivot_index - 1] != numbers[pivot_index]:
            for triplet in find_two_sum(numbers, pivot_index):
                result.append(triplet)

    return result


def find_two_sum(numbers: List[int], target_index: int) -> List[List[int]]:
    seen = set()
    n = len(numbers)
    target = numbers[target_index]
    j = target_index + 1
    while j < n:
        complement = -target - numbers[j]
        if complement in seen:
            yield [target, numbers[j], complement]

            while j + 1 < n and numbers[j] == numbers[j + 1]:
                j += 1

        seen.add(numbers[j])
        j += 1
