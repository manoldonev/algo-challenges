
import unittest

from next_greater_element_i import next_greater_element


class NextGreaterElementITests(unittest.TestCase):

    """Tests for next greater element i challenge."""

    def test_case_1(self):
        self.assertEqual(next_greater_element(
            [4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
