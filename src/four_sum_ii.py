
"""4Sum II"""

from collections import Counter
from typing import List


def count_four_sum(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """https://leetcode.com/problems/4sum-ii/"""

    result = 0
    counter = Counter()
    a_counter = Counter(A)
    b_counter = Counter(B)
    c_counter = Counter(C)
    d_counter = Counter(D)

    for a in a_counter:
        for b in b_counter:
            counter[a+b] += a_counter[a] * b_counter[b]

    for c in c_counter:
        for d in d_counter:
            complement = -(c+d)
            if complement in counter:
                result += counter[complement] * c_counter[c] * d_counter[d]

    return result
