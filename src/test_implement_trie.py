
import unittest

from implement_trie import Trie, Trie2


class ImplementTrieTests(unittest.TestCase):
    """Tests for implement trie challenge."""

    def test_case_1(self):
        trie = Trie()
        trie.insert('apple')
        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.starts_with('app'))
        trie.insert('app')
        self.assertTrue(trie.search('app'))

    def test_case_2(self):
        trie = Trie2()
        trie.insert('apple')
        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.starts_with('app'))
        trie.insert('app')
        self.assertTrue(trie.search('app'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
