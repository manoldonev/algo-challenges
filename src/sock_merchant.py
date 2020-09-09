
""" Sock Merchant"""

from collections import Counter


def sock_merchant(n, array):
    """https://www.hackerrank.com/challenges/sock-merchant"""
    socks_counter = Counter(array)
    return sum(i // 2 for i in socks_counter.values())


if __name__ == '__main__':
    print(sock_merchant(7, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
