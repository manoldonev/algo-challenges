
import unittest

from find_peak_element_2d import find_peak_element


class FindPeakElement2DTests(unittest.TestCase):
    """Tests for find peak element 2D tests"""

    def test_case_1(self):
        self.assertEqual(find_peak_element([[10, 12, 14, 11, 7],
                                            [7, 11, 16, 18, 20],
                                            [11, 15, 10, 8, 6],
                                            [20, 11, 25, 12, 10]]), (3, 2))

    def test_case_2(self):
        self.assertEqual(find_peak_element([[10, 12, 14, 11, 7],
                                            [7, 11, 16, 18, 20],
                                            [11, 15, 10, 8, 6],
                                            [20, 27, 25, 12, 10]]), (3, 1))

    def test_case_3(self):
        self.assertEqual(find_peak_element([[10, 12, 14, 11, 7],
                                            [7, 11, 16, 18, 20],
                                            [11, 15, 10, 8, 6],
                                            [32, 27, 25, 12, 10]]), (3, 0))

    def test_case_4(self):
        self.assertEqual(find_peak_element([[10, 12, 14, 11, 7],
                                            [7, 11, 16, 18, 20],
                                            [41, 15, 10, 8, 6],
                                            [32, 27, 25, 12, 10]]), (2, 0))

    def test_case_5(self):
        self.assertEqual(find_peak_element([[10, 12, 14, 11, 7],
                                            [7, 11, 16, 18, 20],
                                            [11, 15, 10, 8, 6],
                                            [32, 11, 25, 26, 30]]), (3, 4))

    def test_case_6(self):
        self.assertEqual(find_peak_element([[10, 12, 14, 11, 7]]), (0, 2))

    def test_case_7(self):
        self.assertEqual(find_peak_element([[10],
                                            [12],
                                            [14],
                                            [11],
                                            [7]]), (2, 0))

    def test_case_8(self):
        self.assertEqual(find_peak_element([[10]]), (0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
