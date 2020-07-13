
"""Luck Balance"""


def luck_balance(k, contests):
    """https://www.hackerrank.com/challenges/luck-balance"""

    remaining_important_losses = k
    total_luck = 0
    for luck, importance in sorted(contests, reverse=True):
        if importance:
            if remaining_important_losses > 0:
                total_luck += luck
                remaining_important_losses -= 1
            else:
                total_luck -= luck
        else:
            total_luck += luck

    return total_luck


print(luck_balance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
