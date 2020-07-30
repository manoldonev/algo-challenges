"""Bit Flip"""


def bit_flip(array):
    """Given a binary array, find the maximum number zeros in an array with one
    flip of a subarray allowed. A flip operation switches all 0s to 1s and 1s
    to 0s."""

    original_zeroes = 0
    current_sum, max_sum = 0, 0
    for value in array:
        if value == 0:
            value = -1
            original_zeroes += 1

        current_sum = max(0, current_sum + value)
        max_sum = max(max_sum, current_sum)

    return original_zeroes + max_sum
