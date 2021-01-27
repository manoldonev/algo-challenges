
"""Contains Duplicate"""

from typing import List


def contains_duplicate(numbers: List[int]) -> bool:
    """https://leetcode.com/problems/contains-duplicate/submissions/"""

    # return len(numbers) > len(set(numbers))
    unique_numbers = set()
    for value in numbers:
        if value in unique_numbers:
            return True

        unique_numbers.add(value)

    return False
