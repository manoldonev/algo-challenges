
"""Flip String to Monotone Increasing"""


def count_min_flips(s: str) -> int:
    """https://leetcode.com/problems/flip-string-to-monotone-increasing"""
    count_one = count_flip = 0
    for char in s:
        if char == '1':
            count_one += 1
        else:
            count_flip = min(count_flip + 1, count_one)

    return count_flip
