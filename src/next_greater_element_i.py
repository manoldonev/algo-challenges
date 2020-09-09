
"""Next Greater Element I"""

from typing import List


def next_greater_element(numbers1: List[int], numbers2: List[int]) -> List[int]:
    """https://leetcode.com/problems/next-greater-element-i/"""

    # monotone decreasing stack
    min_stack = []
    map_helper = {}
    for value in numbers2:
        while min_stack and min_stack[-1] <= value:
            map_helper[min_stack[-1]] = value
            min_stack.pop()

        min_stack.append(value)

    result = []
    for value in numbers1:
        result.append(map_helper[value] if value in map_helper else -1)

    return result
