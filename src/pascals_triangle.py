
"""Pascal's Triangle"""

from typing import List


def generate(rows: int) -> List[List[int]]:
    """https://leetcode.com/problems/pascals-triangle/"""
    triangle = []

    for row_number in range(rows):
        row = [1 for _ in range(row_number + 1)]
        # first and last row elements are always 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[row_number - 1][j - 1] + \
                triangle[row_number - 1][j]

        triangle.append(row)

    return triangle
