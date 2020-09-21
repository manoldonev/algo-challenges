
"""House Robber II"""

from typing import List

import house_robber


def rob(numbers: List[int]) -> int:
    """https://leetcode.com/problems/house-robber-ii/"""
    n = len(numbers)
    if n == 1:
        return house_robber.rob(numbers)

    return max(house_robber.rob(numbers[:n-1]), house_robber.rob(numbers[1:]))
