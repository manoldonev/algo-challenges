
"""Minimum Window Substring"""

import sys
from collections import Counter


def minimum_window_substring(string: str, lookup: str) -> str:
    """https://leetcode.com/problems/minimum-window-substring"""

    lookup_counter = Counter(lookup)
    distinct_symbols_to_find = len(lookup_counter)
    fast, slow = 0, 0
    minimum_window = (-sys.maxsize + 1, sys.maxsize)
    for index, char in enumerate(string):
        fast = index
        if char not in lookup_counter:
            continue

        lookup_counter[char] -= 1
        if lookup_counter[char] == 0:
            distinct_symbols_to_find -= 1

        while distinct_symbols_to_find == 0:
            if minimum_window[1] - minimum_window[0] > fast - slow:
                minimum_window = (slow, fast)

            symbol_to_drop = string[slow]
            slow += 1
            if symbol_to_drop not in lookup_counter:
                continue

            lookup_counter[symbol_to_drop] += 1
            if lookup_counter[symbol_to_drop] == 1:
                distinct_symbols_to_find += 1

    if minimum_window == (-sys.maxsize + 1, sys.maxsize):
        return ""

    return string[minimum_window[0]: minimum_window[1] + 1]
