
import unittest

from character_replacement import character_replacement


class CharacterReplacementTests(unittest.TestCase):
    """Tests for character replacement challenge."""

    def test_case_1(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)

    def test_case_2(self):
        self.assertEqual(character_replacement("BBBB", 1), 4)

    def test_case_3(self):
        self.assertEqual(character_replacement("AABABBA", 1), 4)

    def test_case_4(self):
        self.assertEqual(character_replacement("CACABBABCBA", 1), 4)

    def test_case_5(self):
        self.assertEqual(character_replacement("AAAB", 0), 3)

    def test_case_6(self):
        self.assertEqual(character_replacement("BAAAB", 2), 5)

    def test_case_7(self):
        self.assertEqual(character_replacement(
            "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
