
import unittest

from delete_and_earn import delete_and_earn


class DeleteAndEarnTests(unittest.TestCase):
    """Tests for delete and earn challenge"""

    def test_case_1(self):
        self.assertEqual(delete_and_earn([3, 4, 2]), 6)

    def test_case_2(self):
        self.assertEqual(delete_and_earn([2, 2, 3, 3, 3, 4]), 9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
