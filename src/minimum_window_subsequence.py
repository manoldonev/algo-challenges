
"""Minimum Window Subsequence"""

import sys


def minimum_window_subsequence(s: str, t: str) -> str:
    """https://leetcode.com/problems/minimum-window-subsequence/"""

    len_s = len(s)
    len_t = len(t)
    dp = [[-1 for col in range(len_t)] for row in range(len_s)]

    for i in range(len_s):
        if s[i] == t[0]:
            dp[i][0] = i
        elif i > 0:
            dp[i][0] = dp[i-1][0]

    for i in range(1, len_s):
        for j in range(1, len_t):
            if s[i] == t[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    min_length = sys.maxsize
    min_start_index = -1
    for i in range(len_s):
        current_start_index = dp[i][len_t - 1]
        if current_start_index == -1:
            continue

        current_length = i - current_start_index + 1
        if current_length < min_length:
            min_length = current_length
            min_start_index = current_start_index

    if min_start_index == -1:
        return ""

    return s[min_start_index:min_start_index + min_length]
