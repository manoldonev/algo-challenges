
"""Candies"""


def candies(n, ratings):
    """https://www.hackerrank.com/challenges/candies"""

    result = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            result[i] = result[i - 1] + 1
        else:
            result[i] = 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            result[i] = max(result[i], result[i + 1] + 1)

    return sum(result)


print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
