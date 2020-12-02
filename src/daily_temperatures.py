
"""Daily Temperatures"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """https://leetcode.com/problems/daily-temperatures/"""

    if not temperatures:
        return []

    n = len(temperatures)
    distances = [0] * n
    # monotone decreasing stack of indices
    min_stack = []

    for index, value in _reverse_enumerate(temperatures):
        # maintain monotone queue invariant
        while min_stack and temperatures[min_stack[-1]] <= value:
            min_stack.pop()

        if min_stack:
            distances[index] = min_stack[-1] - index

        min_stack.append(index)

    return distances


def _reverse_enumerate(l):
    return zip(range(len(l) - 1, -1, -1), reversed(l))
