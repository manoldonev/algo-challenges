
"""Tries Package"""

from collections import defaultdict


class TriesNode(object):
    __slots__ = "value", "usage_count", "children"

    def __init__(self, value=""):
        self.value = value
        self.usage_count = 0
        self.children = defaultdict(TriesNode)

    def add(self, char):
        if self.usage_count == 1:
            self.value += char
            return self

        child = self.children[char]
        if child.usage_count == 1 and len(child.value) > 1:
            child.split_suffix()

        child.value = char
        child.usage_count += 1

        return child

    def split_suffix(self):
        child = self.children[self.value[1]]
        child.value = self.value[1:]
        child.usage_count += 1


class Tries(object):
    """https://www.hackerrank.com/challenges/ctci-contacts"""

    def __init__(self):
        self.root = TriesNode("*")

    def add(self, word):
        node = self.root
        for char in word:
            node = node.add(char)

    def find(self, partial):
        node = self.root
        for index, char in enumerate(partial):
            if not node.children.has_key(char):
                return 0

            node = node.children[char]

            if node.usage_count == 1 and \
                    node.value.startswith(partial[index:]):
                return 1

        return node.usage_count
