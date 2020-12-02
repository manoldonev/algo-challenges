
"""Number of Longest Increasing Subsequence"""

from typing import List


def find_number_of_lis(numbers: List[int]) -> int:
    """https://leetcode.com/problems/number-of-longest-increasing-subsequence/"""

    # [length, count] of longest increasing subsequence ending at index i
    dp = [[1, 1] for _ in range(len(numbers))]
    max_length = 1
    for i, value in enumerate(numbers):
        current_max_length = 1
        count = 0
        for j in range(i):
            if numbers[j] < value:
                if dp[j][0] + 1 > current_max_length:
                    current_max_length = dp[j][0] + 1
                    count = 0

                if dp[j][0] == current_max_length - 1:
                    count += dp[j][1]

        dp[i] = [current_max_length, max(count, dp[i][1])]
        max_length = max(max_length, current_max_length)

    return sum([item[1] for item in dp if item[0] == max_length])
