
"""Next Greater Element II"""

from typing import List


def next_greater_element(numbers: List[int]) -> List[int]:
    """https://leetcode.com/problems/next-greater-element-ii/"""

    n = len(numbers)
    # monotone decreasing stack
    min_stack = []
    result = [-1] * n
    for i in range(2 * n):
        i_mod_n = i % n
        value = numbers[i_mod_n]
        while min_stack and numbers[min_stack[-1]] < value:
            result[min_stack[-1]] = value
            min_stack.pop()

        min_stack.append(i_mod_n)

    return result
