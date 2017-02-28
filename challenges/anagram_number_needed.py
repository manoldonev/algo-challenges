
from collections import Counter


def number_needed(a, b):
    """https://www.hackerrank.com/challenges/ctci-making-anagrams"""

    a_b_counter = Counter(a) & Counter(b)
    return len(a) + len(b) - 2 * sum(a_b_counter.values())


# def number_needed(a, b):
#     a_counter = Counter(a)
#     b_counter = Counter(b)
#     a_b_counter = a_counter & b_counter

#     return sum(value for value in (a_counter - a_b_counter).itervalues()) + \
#         sum(value for value in (b_counter - a_b_counter).itervalues())
