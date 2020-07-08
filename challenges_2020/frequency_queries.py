
"""Frequence Queries"""

from collections import Counter


def frequency_queries(queries):
    """https://www.hackerrank.com/challenges/frequency-queries"""

    counter = Counter()
    reverse_counter = Counter()
    output = []
    for operation, value in queries:
        if operation == 1:
            if reverse_counter[counter[value]] > 0:
                reverse_counter[counter[value]] -= 1

            counter[value] += 1
            reverse_counter[counter[value]] += 1
        elif operation == 2:
            if counter[value] > 0:
                reverse_counter[counter[value]] -= 1
                counter[value] -= 1
                reverse_counter[counter[value]] += 1
        else:
            output.append(int(reverse_counter[value] > 0))
    return output


print(frequency_queries([(3, 4),
                         (2, 1003),
                         (1, 16),
                         (3, 1)]))
