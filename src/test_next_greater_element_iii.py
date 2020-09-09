
import unittest

from next_greater_element_iii import next_greater_element


class NextGreaterElementIIITests(unittest.TestCase):

    """Tests for next greater element iii challenge."""

    def test_case_1(self):
        self.assertEqual(next_greater_element(12), 21)

    def test_case_2(self):
        self.assertEqual(next_greater_element(21), -1)

    def test_case_3(self):
        self.assertEqual(next_greater_element(12443322), 13222344)

    def test_case_4(self):
        self.assertEqual(next_greater_element(2147483647), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
