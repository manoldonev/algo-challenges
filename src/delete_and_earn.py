
"""Delete and Earn"""

from typing import List
from collections import Counter


def delete_and_earn(numbers: List[int]) -> int:
    """https://leetcode.com/problems/delete-and-earn/"""

    counter = Counter(numbers)
    using, avoid = 0, 0

    previous_value = None
    for value in sorted(counter):
        if value - 1 == previous_value:
            avoid, using = max(avoid, using), value * counter[value] + avoid
        else:
            avoid, using = max(avoid, using), value * \
                counter[value] + max(avoid, using)

        previous_value = value

    return max(avoid, using)
