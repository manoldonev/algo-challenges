
"""Counting Valleys"""


def counting_valleys(n, s):
    """https://www.hackerrank.com/challenges/counting-valleys"""

    valley_count = 0
    level = 0

    for step in s:
        if step == 'D':
            level -= 1
        else:
            level += 1

        if level == 0 and step == 'U':
            valley_count += 1

    return valley_count


if __name__ == '__main__':
    print(counting_valleys(8, "UDDDUDUU"))
