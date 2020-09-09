
"""Longest Substring Length with At Most K Distinct Characters (leetcode locked)"""


def find_length(s: str, k: int = 2) -> int:
    """https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters"""

    counter = {}
    fast, slow = 0, 0
    distinct_found = 0
    max_length = 0

    for index, char in enumerate(s):
        fast = index

        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
            distinct_found += 1

        while distinct_found > k:
            trailing_symbol = s[slow]
            counter[trailing_symbol] -= 1
            if counter[trailing_symbol] == 0:
                del counter[trailing_symbol]
                distinct_found -= 1

            slow += 1

        max_length = max(max_length, fast - slow + 1)

    return max_length


print(find_length("abbacdfghiababababad"))
