
"""132 Pattern"""

import sys

from typing import List


def find_132_pattern(numbers: List[int]) -> bool:
    """https://leetcode.com/problems/132-pattern/"""

    # search for subsequence (s1, s2, s3) with s1 < s3 < s2
    s3 = -sys.maxsize
    stack = []
    for value in reversed(numbers):
        # s1 candidate
        if value < s3:
            return True

        while stack and stack[-1] < value:
            s3 = stack.pop()

        # s2 is at the top of the stack
        stack.append(value)

    return False
