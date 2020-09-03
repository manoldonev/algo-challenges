
"""Daily Temperatures"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    if not temperatures:
        return []

    n = len(temperatures)
    distances = [0] * n
    # monotone decreasing queue of indices
    min_queue = []

    for index, value in _reverse_enumerate(temperatures):
        # maintain monotone queue invariant
        while min_queue and temperatures[min_queue[-1]] <= value:
            min_queue.pop()

        if min_queue:
            distances[index] = min_queue[-1] - index

        min_queue.append(index)

    return distances


def _reverse_enumerate(l):
    return zip(range(len(l) - 1, -1, -1), reversed(l))
