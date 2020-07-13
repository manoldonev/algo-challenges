
"""Greedy Florist"""


def get_minimum_cost(k, costs):
    """https://www.hackerrank.com/challenges/greedy-florist/"""

    purchased_flowers = [0] * k
    minimum_cost = 0
    for original_price in sorted(costs, reverse=True):
        purchase_amount, buyer_index = _calculate_next_purchase(
            purchased_flowers, original_price)
        purchased_flowers[buyer_index] += 1
        minimum_cost += purchase_amount

    return minimum_cost


def _calculate_next_purchase(purchased_flowers, cost):
    return min(((value + 1) * cost, index)
               for index, value in enumerate(purchased_flowers))


print(get_minimum_cost(3, [1, 3, 5, 7, 9]))
