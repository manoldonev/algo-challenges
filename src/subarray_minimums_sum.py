
"""Sum of Subarray Minimums"""

from typing import List


def sum_subarray_minimums(numbers: List[int]) -> int:
    """https://leetcode.com/problems/sum-of-subarray-minimums/"""

    # monotone increasing stack
    max_stack = []
    n = len(numbers)
    # left[i] = distance from i to previous smaller element
    left = [i + 1 for i in range(n)]
    # right[i] = distance from i to next smaller element
    right = [n - i for i in range(n)]

    for i, value in enumerate(numbers):
        while max_stack and numbers[max_stack[-1]] > value:
            right[max_stack[-1]] = i - max_stack[-1]
            max_stack.pop()

        if max_stack:
            left[i] = i - max_stack[-1]

        max_stack.append(i)

    mod = 10**9 + 7

    # [L...min], [min...R] -> min is a minimum of dist(L) * dist(R) subarrays
    return sum(min*l*r for min, l, r in zip(numbers, left, right)) % mod
