
"""Two Strings"""


def two_strings(s1, s2):
    """https://www.hackerrank.com/challenges/two-strings"""

    set1 = set(s1)
    set2 = set(s2)

    return "YES" if len(set1 & set2) > 0 else "NO"


if __name__ == '__main__':
    print(two_strings("hello", "world"))
