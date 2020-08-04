
"""Longest Substring Without Repeating Characters"""


def maximum_distinct_substring_length(s: str) -> int:
    """https://leetcode.com/problems/longest-substring-without-repeating-characters"""

    char_to_index_map = {}
    fast, slow = 0, 0
    max_substring_length = 0

    for index, char in enumerate(s):
        fast = index

        if char in char_to_index_map:
            slow = max(slow, char_to_index_map[char] + 1)

        char_to_index_map[char] = index

        max_substring_length = max(max_substring_length, fast - slow + 1)

    return max_substring_length
