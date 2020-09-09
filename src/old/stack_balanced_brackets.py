
"""Balanced Brackets Package"""


def is_matched(expression):
    """https://www.hackerrank.com/challenges/ctci-balanced-brackets"""

    stack = []
    pairs = {"(": ")", "{": "}", "[": "]"}

    for c in expression:
        if c in pairs:
            stack.append(pairs[c])
        elif not stack or c != stack.pop():
            return False

    return not stack
