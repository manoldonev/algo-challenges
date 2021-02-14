
import unittest

from strobogrammatic_number_ii import find_strobogrammatic


class StrobogrammaticNumberIiTests(unittest.TestCase):
    """Tests for strobogrammatic number ii challenge"""

    def test_case_1(self):
        self.assertEqual(find_strobogrammatic(1), ['0', '1', '8'])

    def test_case_2(self):
        self.assertEqual(find_strobogrammatic(2), ['11', '88', '69', '96'])

    def test_case_3(self):
        self.assertEqual(find_strobogrammatic(3), [
            '101', '609', '808', '906', '111', '619',
            '818', '916', '181', '689', '888', '986'])

    def test_case_4(self):
        self.assertEqual(find_strobogrammatic(4), [
            '1001', '6009', '8008', '9006', '1111', '6119', '8118',
            '9116', '1881', '6889', '8888', '9886', '1691', '6699',
            '8698', '9696', '1961', '6969', '8968', '9966'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
