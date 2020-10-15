
"""Two Sum"""

from typing import List


def find_two_sum(numbers: List[int], target: int) -> List[int]:
    """https://leetcode.com/problems/two-sum/"""

    numbers_map = {}
    for index, number in enumerate(numbers):
        pair_number = target - number
        if pair_number in numbers_map:
            return [numbers_map[pair_number], index]

        numbers_map[number] = index
