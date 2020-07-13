
"""Minimum Absolute Difference"""


def minimum_absolute_difference(arr):
    """https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array"""

    sorted_array = sorted(arr)
    return min(abs(x - y) for x, y in zip(sorted_array, sorted_array[1:]))


print(minimum_absolute_difference([1, -3, 71, 68, 17]))
