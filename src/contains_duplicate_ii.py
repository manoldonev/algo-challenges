
"""Contains Duplicate II"""

from typing import List


def contains_nearby_duplicate(numbers: List[int], k: int) -> bool:
    """https://leetcode.com/problems/contains-duplicate-ii/"""
    mapping = {}

    for index, value in enumerate(numbers):
        if value in mapping and index - mapping[value] <= k:
            return True

        mapping[value] = index

    return False
