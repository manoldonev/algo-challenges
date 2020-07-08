
""" Jumping on clouds"""


def jumping_on_clouds(array):
    """https://www.hackerrank.com/challenges/jumping-on-the-clouds"""

    jumps = 0
    i = 0
    n = len(array)
    while i < n - 1:
        jumps += 1
        if i < n - 2 and array[i + 2] == 0:
            i = i + 2
        else:
            i += 1

    return jumps


print(jumping_on_clouds([0, 0, 0, 1, 0, 0]))
