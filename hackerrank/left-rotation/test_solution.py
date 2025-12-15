import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from solution import rotLeft

class TestLeftRotation(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.input_dir = os.path.join(self.test_dir, 'tests', 'input')
        self.output_dir = os.path.join(self.test_dir, 'tests', 'output')

    def load_test_case(self, filename):
        input_path = os.path.join(self.input_dir, filename)
        output_filename = filename.replace('input', 'output')
        output_path = os.path.join(self.output_dir, output_filename)

        if not os.path.exists(output_path):
            return None, None

        with open(input_path, 'r') as f:
            lines = f.readlines()
            n, d = map(int, lines[0].split())
            a = list(map(int, lines[1].split()))

        with open(output_path, 'r') as f:
            expected = list(map(int, f.read().split()))

        return (a, d), expected

    def test_sample_case_00(self):
        (a, d), expected = self.load_test_case('input00.txt')
        self.assertIsNotNone(expected, "Output file not found")
        result = rotLeft(a, d)
        self.assertEqual(result, expected)

    def test_basic_rotation(self):
        a = [1, 2, 3, 4, 5]
        d = 2
        expected = [3, 4, 5, 1, 2]
        self.assertEqual(rotLeft(a, d), expected)

    def test_full_rotation(self):
        a = [1, 2, 3]
        d = 3
        expected = [1, 2, 3]
        self.assertEqual(rotLeft(a, d), expected)

    def test_zero_rotation(self):
        a = [1, 2, 3]
        d = 0
        expected = [1, 2, 3]
        self.assertEqual(rotLeft(a, d), expected)

if __name__ == '__main__':
    unittest.main()
