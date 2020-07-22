

def find_min_distinct_subarray(array):
    distinct_count = len(set(array))
    last_seen = {}
    sequence_start = None
    sequence_end = None
    for index, value in enumerate(array):
        last_seen[value] = index
        if len(last_seen) < distinct_count:
            continue

        if sequence_end is None:
            sequence_start = min(last_seen.values())
            sequence_end = index
            continue

        candidate_start = min(last_seen.values())
        candidate_end = max(last_seen.values())

        if candidate_end - candidate_start <= sequence_end - sequence_start:
            sequence_start = candidate_start
            sequence_end = candidate_end

    return array[sequence_start:sequence_end + 1]


if __name__ == '__main__':
    # [1, 2, 2, 3]
    print(find_min_distinct_subarray([1, 2, 1, 2, 2, 3, 2]))

    # [2, 3, 1]
    print(find_min_distinct_subarray(
        [2, 2, 1, 2, 2, 3, 1, 1, 2, 2, 1, 2, 2, 3]))

    # [2, 1, 1, 1, 3]
    print(find_min_distinct_subarray(
        [2, 2, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 1]))

    # [1, 2, 2, 2, 2, 2, 3]
    print(find_min_distinct_subarray([1, 2, 2, 2, 2, 2, 3]))

    # [3, 2, 2, 1]
    print(find_min_distinct_subarray(
        [3, 1, 1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 1]))
