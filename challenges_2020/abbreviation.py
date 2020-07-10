
"""Abbreviation"""


def abbreviation(a, b):
    """https://www.hackerrank.com/challenges/abbr"""

    n = len(b)
    m = len(a)

    memo = [[False]*(m + 1) for _ in range(n + 1)]
    memo[0][0] = True

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j > 0:
                memo[i][j] = a[j - 1].islower() and memo[i][j - 1]
            elif i > 0 and j > 0:
                if a[j - 1] == b[i - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                elif a[j - 1].upper() == b[i - 1]:
                    memo[i][j] = memo[i - 1][j - 1] or memo[i][j - 1]
                elif a[j - 1].islower():
                    memo[i][j] = memo[i][j - 1]
                else:
                    memo[i][j] = False

    return "YES" if memo[n][m] else "NO"


print(abbreviation("daBcd", "ABC"))
