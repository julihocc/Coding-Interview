import unittest
import sys
import os

# Add the parent directory to sys.path to import the solution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions.original import target_index_search

class TestTargetIndexSearch(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        expected = 2
        self.assertEqual(target_index_search(nums, target), expected)

    def test_example_2(self):
        nums = [2, 4, 6, 8, 10, 12, 14, 16]
        target = 16
        expected = 7
        self.assertEqual(target_index_search(nums, target), expected)

    def test_target_not_found(self):
        nums = [1, 3, 5, 7]
        target = 4
        expected = -1
        self.assertEqual(target_index_search(nums, target), expected)

    def test_empty_array(self):
        nums = []
        target = 1
        expected = -1
        self.assertEqual(target_index_search(nums, target), expected)

    def test_single_element_found(self):
        nums = [5]
        target = 5
        expected = 0
        self.assertEqual(target_index_search(nums, target), expected)

    def test_single_element_not_found(self):
        nums = [5]
        target = 3
        expected = -1
        self.assertEqual(target_index_search(nums, target), expected)

    def test_negative_numbers(self):
        nums = [-10, -5, 0, 5, 10]
        target = -5
        expected = 1
        self.assertEqual(target_index_search(nums, target), expected)

if __name__ == '__main__':
    unittest.main()
