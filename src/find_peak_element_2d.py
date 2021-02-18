
"""Find Peak Element 2D"""

from typing import List, Tuple


def find_peak_element(numbers: List[List[int]]) -> Tuple:
    """
    2D version of https://leetcode.com/problems/find-peak-element/
    Find a peak element in a n x m integer matrix.
    In 2D (i,j) is a peak element if and only if it is strictly
    greater than elements (i, j - 1), (i, j + 1), (i - 1, j), and (i + 1, j)
    (if such elements exists; otherwise assume their value is -eternity)
    """

    left = 0
    right = len(numbers[0]) - 1
    while left < right:
        col = (left + right) // 2
        row = _find_column_global_peak(numbers, col)
        if numbers[row][col] < numbers[row][col - 1]:
            right = col - 1
        elif numbers[row][col] < numbers[row][col + 1]:
            left = col + 1
        else:
            return row, col

    return _find_column_global_peak(numbers, left), left


def _find_column_global_peak(numbers: List[List[int]], col: int) -> int:
    n = len(numbers)

    global_peak_index = -1

    for i in range(n - 1):
        if numbers[i][col] > numbers[i + 1][col] and \
                global_peak_index < 0 or \
                numbers[i][col] > numbers[global_peak_index][col]:
            global_peak_index = i

    if numbers[n - 1][col] > numbers[global_peak_index][col] or \
            global_peak_index < 0:
        global_peak_index = n - 1

    return global_peak_index
