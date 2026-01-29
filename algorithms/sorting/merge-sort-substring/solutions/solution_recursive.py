"""Recursive merge sort with substring comparison.

This solution implements merge sort with a custom comparison that only
considers the first 3 characters of each string during the merge operation.
"""

from typing import List


class Solution:
    """Recursive merge sort with substring comparison."""

    def __init__(self, strings: List[str]):
        """Initialize with the list of strings to sort.
        
        Args:
            strings: A list of strings to sort by first 3 characters.
        """
        self.strings = strings

    def merge_sort_substring(self) -> List[str]:
        """Sort strings by their first 3 characters using recursive merge sort.
        
        Returns:
            A new sorted list of strings.
        """
        return self._merge_sort_recursive(self.strings)
    
    def _merge_sort_recursive(self, arr: List[str]) -> List[str]:
        """Recursively sort an array using merge sort with substring comparison.
        
        Base case: Arrays with 0 or 1 elements are already sorted.
        Recursive case: Divide array in half, sort each half, then merge
        using substring comparison.
        
        Args:
            arr: The array of strings to sort.
            
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
        
        # Combine: merge the sorted halves using substring comparison
        return self._merge(left_half, right_half)
    
    def _merge(self, left: List[str], right: List[str]) -> List[str]:
        """Merge two sorted arrays using substring comparison.
        
        Compares strings based on their first 3 characters only.
        If a string has fewer than 3 characters, uses the entire string.
        
        Args:
            left: First sorted array.
            right: Second sorted array.
            
        Returns:
            A new sorted array containing all elements from both inputs.
        """
        result = []
        i = j = 0
        
        # Compare elements from both arrays using first 3 characters
        while i < len(left) and j < len(right):
            # KEY MODIFICATION: Compare only first 3 characters
            if left[i][:3] <= right[j][:3]:
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
        instance = SolutionClass(list(case.strings))
        result = instance.merge_sort_substring()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
