
"""House Robber"""

from typing import List


def rob(numbers: List[int]) -> int:
    """https://leetcode.com/problems/house-robber/"""

    # f(k) = max(f(k – 2) + numbers[k], f(k – 1))
    previous_max, current_max = 0, 0
    for value in numbers:
        current_max, previous_max = max(
            previous_max + value, current_max), current_max

    return current_max
