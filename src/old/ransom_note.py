
"""Ransom Note Package"""

from collections import Counter


def ransom_note(magazine, ransom):
    """https://www.hackerrank.com/challenges/ctci-ransom-note"""

    magazine_counter = Counter(magazine)
    ransom_counter = Counter(ransom)

    if magazine_counter & ransom_counter == ransom_counter:
        return True

    return False
