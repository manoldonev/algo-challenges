
"""Move Zeroes"""

from typing import List


def move_zeroes(numbers: List[int]) -> None:
    """https://leetcode.com/problems/move-zeroes/"""

    last_non_zero_index = -1
    for index, value in enumerate(numbers):
        if value:
            if last_non_zero_index < 0:
                numbers[0], numbers[index] = numbers[index], numbers[0]
                last_non_zero_index = 0
            elif last_non_zero_index < index:
                numbers[last_non_zero_index +
                        1], numbers[index] = numbers[index], numbers[last_non_zero_index + 1]
                last_non_zero_index += 1
