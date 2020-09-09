
import unittest

from longest_subarray_abs_diff import longest_subarray, longest_subarray_bidirectional_pointer


class LongestSubarrayAbsoluteDiffTests(unittest.TestCase):

    """Tests for longest subarray with absolute diff less than limit challenge."""

    def test_case_1(self):
        self.assertEqual(longest_subarray([8, 2, 4, 7], 4), 2)

    def test_case_2(self):
        self.assertEqual(longest_subarray(
            [
                24, 12, 71, 33, 5, 87, 10, 11, 3, 58, 2, 97, 97, 36, 32, 35, 15,
                80, 24, 45, 38, 9, 22, 21, 33, 68, 22, 85, 35, 83, 92, 38, 59, 90,
                42, 64, 61, 15, 4, 40, 50, 44, 54, 25, 34, 14, 33, 94, 66, 27, 78,
                56, 3, 29, 3, 51, 19, 5, 93, 21, 58, 91, 65, 87, 55, 70, 29, 81,
                89, 67, 58, 29, 68, 84, 4, 51, 87, 74, 42, 85, 81, 55, 8, 95, 39
            ], 87), 25)

    def test_case_3(self):
        self.assertEqual(longest_subarray([8], 1), 1)

    def test_case_4(self):
        self.assertEqual(longest_subarray([], 0), 0)

    def test_case_5(self):
        self.assertEqual(
            longest_subarray_bidirectional_pointer([8, 2, 4, 7], 4), 2)

    def test_case_6(self):
        self.assertEqual(longest_subarray_bidirectional_pointer(
            [
                24, 12, 71, 33, 5, 87, 10, 11, 3, 58, 2, 97, 97, 36, 32, 35, 15,
                80, 24, 45, 38, 9, 22, 21, 33, 68, 22, 85, 35, 83, 92, 38, 59, 90,
                42, 64, 61, 15, 4, 40, 50, 44, 54, 25, 34, 14, 33, 94, 66, 27, 78,
                56, 3, 29, 3, 51, 19, 5, 93, 21, 58, 91, 65, 87, 55, 70, 29, 81,
                89, 67, 58, 29, 68, 84, 4, 51, 87, 74, 42, 85, 81, 55, 8, 95, 39
            ], 87), 25)

    def test_case_7(self):
        self.assertEqual(longest_subarray_bidirectional_pointer([8], 1), 1)

    def test_case_8(self):
        self.assertEqual(longest_subarray_bidirectional_pointer([], 0), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
