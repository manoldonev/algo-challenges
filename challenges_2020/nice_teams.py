"""Nice Teams"""

import math
from heapq import heappop, heapify


def max_pairs(skill_levels, min_diff):
    """Returns an integer representing max number of pairs with at least
    min_diff difference between pair values."""

    skill_levels.sort()
    n = len(skill_levels)
    n_by_2 = math.ceil(n / 2)
    heap = skill_levels[:n_by_2]
    pair_heap = skill_levels[n_by_2:]
    heapify(heap)
    heapify(pair_heap)

    pairs = 0
    heap_n = n_by_2
    pair_heap_n = n - n_by_2
    while heap_n > 0 and pair_heap_n > 0:
        if heap[0] + min_diff <= pair_heap[0]:
            pairs += 1
            heappop(heap)
            heap_n -= 1

        heappop(pair_heap)
        pair_heap_n -= 1

    return pairs


print(max_pairs([3, 4, 5, 2, 1, 1], 3))
