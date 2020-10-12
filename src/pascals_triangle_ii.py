
"""Pascal's Triangle II"""

from typing import List
from operator import add


def get_row(row_index: int) -> List[int]:
    """https://leetcode.com/problems/pascals-triangle-ii/"""

    current_row = [1]
    for _ in range(1, row_index + 1):
        map_ = map(add, [0] + current_row, current_row + [0])
        current_row = list(map_)

    return current_row
