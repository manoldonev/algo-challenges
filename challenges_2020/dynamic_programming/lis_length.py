"""Length of Longest Increasing Subsequence"""

from typing import List


def find_length_of_lis(numbers: List[int]) -> int:
    """https://leetcode.com/problems/longest-increasing-subsequence/"""
    if not numbers:
        return 0

    n = len(numbers)
    # length of longest increasing subsequence ending at index i
    dp = [0] * n
    dp[0] = 1

    max_length = 1
    for i in range(1, n):
        max_value = 0
        for j in range(i):
            if numbers[j] < numbers[i]:
                max_value = max(max_value, dp[j])

        dp[i] = max_value + 1
        max_length = max(max_length, dp[i])

    return max_length
