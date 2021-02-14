
""" Strobogrammatic Number II"""

from typing import List


def find_strobogrammatic(n: int) -> List[str]:
    """https://leetcode.com/problems/strobogrammatic-number-ii"""

    if n == 1:
        return ['0', '1', '8']

    return [num
            for num in _find_strobogrammatic_helper(n)
            if num[0] != '0' and num[-1] != '0']


def _find_strobogrammatic_helper(n: int) -> List[str]:
    if n == 1:
        return ['0', '1', '8']

    if n == 2:
        return ['00', '11', '88', '69', '96']

    rotated_digits = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    return [digit + partial + rotated_digit
            for partial in _find_strobogrammatic_helper(n - 2)
            for digit, rotated_digit in rotated_digits.items()]
