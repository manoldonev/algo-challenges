
"""Implement Trie (Prefix Tree)"""

from collections import defaultdict

END_MARKER = '__END__'


class TrieNode:
    """Trie node implementation"""
    __slots__ = '__is_end', 'children'

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.__is_end = False

    def get(self, char: str) -> 'TrieNode':
        return self.children[char]

    def set(self, char: str, node: 'TrieNode') -> None:
        self.children[char] = node

    def contains_key(self, char: str) -> bool:
        return char in self.children

    @property
    def is_end(self) -> bool:
        return self.__is_end

    @is_end.setter
    def is_end(self, end: bool) -> None:
        self.__is_end = end


class Trie:
    """https://leetcode.com/problems/implement-trie-prefix-tree/"""
    __slots__ = 'root'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            node = node.get(letter)

        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            if not node.contains_key(letter):
                return False

            node = node.get(letter)

        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if any word in the trie starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            if not node.contains_key(letter):
                return False

            node = node.get(letter)

        return True


class Trie2:
    """Simple trie implementation based on dictionary"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        level = self.store
        for letter in word:
            if letter not in level:
                level[letter] = {}

            level = level[letter]

        level[END_MARKER] = END_MARKER

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        level = self.store
        for letter in word:
            if letter not in level:
                return False

            level = level[letter]

        if END_MARKER in level:
            return True

        return False

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if any word in the trie starts with the given prefix.
        """
        level = self.store
        for letter in prefix:
            if letter not in level:
                return False

            level = level[letter]

        return True
