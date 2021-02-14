
"""Valid Mountain Array"""


def is_valid_mountain_array(arr):
    """https://leetcode.com/problems/valid-mountain-array"""

    n = len(arr)
    if n < 3:
        return False

    left = 0
    right = n - 1

    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    if left in (0, right):
        return False

    while left < right and arr[left] > arr[left + 1]:
        left += 1

    return left == right
