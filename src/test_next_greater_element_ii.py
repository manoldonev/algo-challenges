
import unittest

from next_greater_element_ii import next_greater_element


class NextGreaterElementIITests(unittest.TestCase):

    """Tests for next greater element ii challenge."""

    def test_case_1(self):
        self.assertEqual(next_greater_element([1, 2, 1]), [2, -1, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
