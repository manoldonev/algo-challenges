
"""Repeated string"""


def repeated_string(s, n):
    """https://www.hackerrank.com/challenges/repeated-string"""

    string_length = len(s)
    m = n // string_length
    remainder = n % string_length
    result = 0
    for index, char in enumerate(s):
        if char != 'a':
            continue

        if index < remainder:
            result += m + 1
        else:
            result += m

    return result


if __name__ == '__main__':
    print(repeated_string("aab", 882787))
