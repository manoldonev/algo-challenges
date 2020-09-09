
"""Maximum Length of Repeated Subarray"""

from typing import List


def find_length(a_list: List[int], b_list: List[int]) -> int:
    """https://leetcode.com/problems/maximum-length-of-repeated-subarray/"""

    m = len(a_list)
    n = len(b_list)

    memo = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a_list[i] == b_list[j]:
                memo[i][j] = memo[i + 1][j + 1] + 1
            else:
                memo[i][j] = 0

    return max(max(row) for row in memo)
