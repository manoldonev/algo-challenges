
"""Longest Repeating Character Replacement"""

from collections import Counter


def character_replacement(s: str, k: int) -> int:
    """https://leetcode.com/problems/longest-repeating-character-replacement"""

    counter = Counter()
    left = 0
    max_length = 0
    current_max_frequency = 0
    for right, char in enumerate(s):
        counter[char] += 1
        current_max_frequency = max(current_max_frequency, counter[char])

        if current_max_frequency + k < right - left + 1:
            trailing_symbol_to_drop = s[left]
            counter[trailing_symbol_to_drop] -= 1

            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
