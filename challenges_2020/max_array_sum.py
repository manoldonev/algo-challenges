
"""Max Array Sum"""

import itertools


def max_subset_sum(arr):
    """https://www.hackerrank.com/challenges/max-array-sum"""

    max_sums = [0, max(0, arr[0])]

    index = 2
    for value in itertools.islice(arr, 1, None):
        max_sums.append(max(max_sums[index - 1], value + max_sums[index - 2]))
        index += 1

    return max_sums[-1]


if __name__ == '__main__':
    print(max_subset_sum([-2, 1, 3, -4, 5]))
