
"""Permutation in String"""

from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    """https://leetcode.com/problems/permutation-in-string/"""
    lookup_symbols = Counter(s1)
    lookup_count = len(s1)
    found_symbols = Counter()
    found_count = 0

    left = 0
    for index, char in enumerate(s2):
        if char in lookup_symbols:
            found_symbols[char] += 1
            found_count += 1
            while found_symbols[char] > lookup_symbols[char]:
                char_to_drop = s2[left]
                if found_symbols[char_to_drop] > 0:
                    found_symbols[char_to_drop] -= 1
                    found_count -= 1

                left += 1
        elif found_symbols:
            found_symbols = Counter()
            found_count = 0
            left = index

        if lookup_count == found_count:
            return True

    return False
