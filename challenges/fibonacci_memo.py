
"""Fibonacci (Memoization) Package"""


def fibonacci(n):
    """https://www.hackerrank.com/challenges/ctci-fibonacci-numbers"""

    return _fibonacci_memo(n)


def _fibonacci_memo(n, cache=None):
    if not cache:
        cache = {0: 0, 1: 1, 2: 1}

    if n in cache:
        return cache[n]

    cache[n] = _fibonacci_memo(n - 1, cache) + _fibonacci_memo(n - 2, cache)

    return cache[n]
