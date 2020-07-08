
"""Sherlock and anagrams"""

from collections import Counter


def sherlock_and_anagrams(s):
    """https://www.hackerrank.com/challenges/sherlock-and-anagrams"""

    string_length = len(s)
    sorted_substrings = ["".join(sorted(s[i:j])) for i in range(
        string_length) for j in range(i + 1, string_length + 1)]

    counter = Counter(sorted_substrings)

    return sum(v * (v - 1) // 2 for v in counter.values() if v > 1)


print(sherlock_and_anagrams("cdcd"))
