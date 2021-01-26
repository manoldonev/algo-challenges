
"""4Sum II"""

from collections import Counter
from typing import List


def count_four_sum(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """https://leetcode.com/problems/4sum-ii/"""

    counter_ab = Counter(a+b for a in A for b in B)
    return sum(counter_ab[-(c+d)] for c in C for d in D)


# def count_four_sum(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#     """https://leetcode.com/problems/4sum-ii/"""

#     return _count_k_sum([A, B, C, D])


# def _count_k_sum(lists: List[List[int]]) -> int:
#     counter = Counter()
#     _add_to_counter(lists, 0, 0, counter)
#     return _count_complements(lists, len(lists) // 2, 0, counter)


# def _add_to_counter(lists: List[List[int]], index: int, half_sum: int, counter: Counter):
#     if index == len(lists) // 2:
#         counter[half_sum] += 1
#     else:
#         for value in lists[index]:
#             _add_to_counter(lists, index + 1, half_sum + value, counter)


# def _count_complements(lists: List[List[int]], index: int, complement: int, counter: Counter) -> int:
#     if index == len(lists):
#         return counter[complement]

#     result = 0
#     for value in lists[index]:
#         result += _count_complements(lists, index + 1,
#                                      complement - value, counter)

#     return result
