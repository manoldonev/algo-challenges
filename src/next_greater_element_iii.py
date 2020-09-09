
"""Next Greater Element III"""


def next_greater_element(number: int) -> int:
    """https://leetcode.com/problems/next-greater-element-iii/"""

    digits = [int(n_char) for n_char in str(number)]
    n = len(digits)

    swap_index = -1
    for index in range(n - 2, -1, -1):
        if digits[index] < digits[index + 1]:
            swap_index = index
            break

    if swap_index == -1:
        return -1

    next_greater_element_index = swap_index + 1
    for index in range(next_greater_element_index + 1, n):
        if digits[index] > digits[swap_index] and \
                digits[index] <= digits[next_greater_element_index]:
            next_greater_element_index = index

    digits[swap_index], digits[next_greater_element_index] = \
        digits[next_greater_element_index], digits[swap_index]

    digits[swap_index + 1:] = reversed(digits[swap_index + 1:])
    result = int(''.join([str(d) for d in digits]))

    if result.bit_length() > 31:
        return -1

    return result
