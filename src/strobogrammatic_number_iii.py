
""" Strobogrammatic Number III"""

from typing import List


def find_strobogrammatic_in_range(low: str, high: str) -> int:
    """https://leetcode.com/problems/strobogrammatic-number-iii"""

    low_count = _find_strobogrammatic_count_below(low, include=False)
    high_count = _find_strobogrammatic_count_below(high)

    return max(high_count - low_count, 0)


def _find_strobogrammatic_count_below(n, include: bool = True) -> int:
    result = 0
    for i in range(1, len(n)):
        result += _find_strobogrammatic_count(i)

    strobogrammatic_numbers_length_n = _find_strobogrammatic(len(n))
    if include:
        strobogrammatic_numbers_length_n = \
            [num
             for num in strobogrammatic_numbers_length_n
             if (len(num) == 1 or num[0] != '0') and num <= n]
    else:
        strobogrammatic_numbers_length_n = \
            [num
             for num in strobogrammatic_numbers_length_n
             if (len(num) == 1 or num[0] != '0') and num < n]

    result += len(strobogrammatic_numbers_length_n)

    return result


def _find_strobogrammatic_count(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 3

    # n is even
    # first digit has four choices 1, 6, 8, 9 (last digit should match)
    # other digits to middle have five choices 0, 1, 6, 8, 9 (rest match)
    if n % 2 == 0:
        return 4 * 5 ** (n//2 - 1)

    # n is odd
    # first digit has four choices 1, 6, 8, 9 (last digit should match)
    # middle digit has three choices 0, 1, 8
    # other digits to middle have five choices 0, 1, 6, 8, 9
    return 3 * 4 * 5 ** (n//2 - 1)


def _find_strobogrammatic(n: int) -> List[str]:
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
            for partial in _find_strobogrammatic(n - 2)
            for digit, rotated_digit in rotated_digits.items()]
