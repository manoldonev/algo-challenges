
"""Minion Game Package"""


def minion_game(string):
    """https://www.hackerrank.com/challenges/the-minion-game"""
    vowels = set("AEIOU")
    n = len(string)
    stuart_score = 0
    kevin_score = 0

    for i, char in enumerate(string):
        if char in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if stuart_score > kevin_score:
        return f"Stuart {stuart_score}"

    if stuart_score < kevin_score:
        return f"Kevin {kevin_score}"

    return "Draw"


if __name__ == '__main__':
    print(minion_game("BANANA"))
