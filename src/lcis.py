
"""Longest Continuous Increasing Subsequence"""

import sys

from typing import List


def find_lcis_length(numbers: List[int]) -> int:
    """https://leetcode.com/problems/longest-continuous-increasing-subsequence/"""

    previous_value = -sys.maxsize
    current_length, max_length = 0, 0
    for value in numbers:
        if value > previous_value:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

        previous_value = value

    return max(max_length, current_length)


if __name__ == "__main__":
    print(find_lcis_length([1, 3, 5, 4, 7]))
    print(find_lcis_length([2, 2, 2, 2, 2]))
    print(find_lcis_length([1, 3, 5, 7]))
    print(find_lcis_length([1, 3, 5, 4, 2, 3, 4, 5]))
    print(find_lcis_length([2, 1, 3]))
