
""" Strobogrammatic Number"""

def is_strobogrammatic(num: str) -> bool:
    """https://leetcode.com/problems/strobogrammatic-number"""

    rotated_digits = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in rotated_digits or \
            num[right] != rotated_digits[num[left]]:
            return False

        left += 1
        right -= 1

    return True
