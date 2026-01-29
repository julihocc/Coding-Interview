"""Recursive merge sort implementation.

This solution implements the classic divide-and-conquer merge sort algorithm
using recursion. It recursively divides the array into halves, sorts each half,
and merges them back together.
"""

from typing import List


class Solution:
    """Recursive merge sort implementation."""

    def __init__(self, nums: List[int]):
        """Initialize with the array to sort.
        
        Args:
            nums: An unsorted list of integers.
        """
        self.nums = nums

    def merge_sort(self) -> List[int]:
        """Sort the array using recursive merge sort.
        
        Returns:
            A new sorted list containing all elements from self.nums.
        """
        return self._merge_sort_recursive(self.nums)
    
    def _merge_sort_recursive(self, arr: List[int]) -> List[int]:
        """Recursively sort an array using merge sort.
        
        Base case: Arrays with 0 or 1 elements are already sorted.
        Recursive case: Divide array in half, sort each half, then merge.
        
        Args:
            arr: The array to sort.
            
        Returns:
            A new sorted array.
        """
        # Base case: arrays with 0 or 1 elements are already sorted
        if len(arr) <= 1:
            return arr
        
        # Divide: find the middle point
        mid = len(arr) // 2
        
        # Conquer: recursively sort both halves
        left_half = self._merge_sort_recursive(arr[:mid])
        right_half = self._merge_sort_recursive(arr[mid:])
        
        # Combine: merge the sorted halves
        return self._merge(left_half, right_half)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays into a single sorted array.
        
        Uses two pointers to compare elements from both arrays and
        build the result in sorted order.
        
        Args:
            left: First sorted array.
            right: Second sorted array.
            
        Returns:
            A new sorted array containing all elements from both inputs.
        """
        result = []
        i = j = 0
        
        # Compare elements from both arrays and add smaller one to result
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements from left array (if any)
        while i < len(left):
            result.append(left[i])
            i += 1
        
        # Add remaining elements from right array (if any)
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result


if __name__ == "__main__":
    import sys
    import os

    # Add the project root to sys.path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))
    
    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        instance = SolutionClass(list(case.nums))
        result = instance.merge_sort()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
