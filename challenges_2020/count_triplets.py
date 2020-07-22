
"""Count triplets"""

from collections import Counter


def count_triplets(arr, r):
    """https://www.hackerrank.com/challenges/count-triplets-1"""

    counter_left = Counter()
    counter_right = Counter(arr)
    result = 0

    for j in arr:
        i = j // r
        k = j * r

        counter_right[j] -= 1

        if counter_left[i] and counter_right[k] and not j % r:
            result += counter_left[i] * counter_right[k]

        counter_left[j] += 1

    return result


if __name__ == '__main__':
    print(count_triplets([1, 5, 5, 25, 125], 5))
