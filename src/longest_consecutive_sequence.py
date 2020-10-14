
"""Longest Consecutive Sequence"""

from typing import List


def find_longest_consecutive_sequence(numbers: List[int]) -> int:
    """https://leetcode.com/problems/longest-consecutive-sequence/"""

    number_set = set(numbers)

    max_length = 0
    for number in number_set:
        if number - 1 in number_set:
            continue

        current = number
        current_length = 1

        while current + 1 in number_set:
            current = current + 1
            current_length += 1

        max_length = max(max_length, current_length)

    return max_length
