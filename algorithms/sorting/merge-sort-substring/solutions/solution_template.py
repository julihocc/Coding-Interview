"""TEMPLATE: Merge sort with substring comparison

Implement merge sort that compares only the first 3 characters of each string.
This demonstrates how to customize the comparison logic in sorting algorithms.

Reference: See ../README.md for full problem description
"""

from typing import List


class YourMergeSortSubstring:
    """Rename and implement this class to match your approach.
    
    Example strategies: NaiveSorter, RecursiveMergeSortSubstring, IterativeMergeSortSubstring
    """

    def __init__(self, strings: List[str]):
        """Initialize with the list of strings to sort.
        
        Args:
            strings: A list of strings to sort by first 3 characters.
        """
        self.strings = strings

    def merge_sort_substring(self) -> List[str]:
        """Sort strings by their first 3 characters.
        
        Expected behavior:
        - Compare only the first 3 characters of each string
        - If a string has < 3 characters, use the entire string
        - Maintain stability (preserve relative order of equal prefixes)
        - Return a new sorted list
        
        Approaches to consider:
        1. Naive: Use sorted() with key=lambda s: s[:3]
        2. Recursive: Modify merge operation to compare s[:3]
        3. Iterative: Bottom-up merge with substring comparison
        
        Returns:
            A sorted list of strings based on first 3 characters.
        """
        # TODO: Implement your sorting strategy
        # For naive: return sorted(self.strings, key=lambda s: s[:3])
        # For recursive: call _merge_sort_recursive(self.strings)
        # For iterative: use loop with progressively larger merge sizes
        raise NotImplementedError
    
    def _merge_sort_recursive(self, arr: List[str]) -> List[str]:
        """Recursively sort an array using merge sort with substring comparison.
        
        Divide-and-conquer approach:
        1. Base case: arrays with 0 or 1 elements are already sorted
        2. Divide: split array at midpoint
        3. Conquer: recursively sort both halves
        4. Combine: merge using substring comparison
        
        Args:
            arr: The array of strings to sort.
            
        Returns:
            A new sorted array.
        """
        # TODO: Implement recursive merge sort
        # Base case: if len(arr) <= 1, return arr
        # Find mid = len(arr) // 2
        # Recursively sort left = arr[:mid] and right = arr[mid:]
        # Return _merge(left, right)
        raise NotImplementedError
    
    def _merge(self, left: List[str], right: List[str]) -> List[str]:
        """Merge two sorted arrays using substring comparison.
        
        KEY MODIFICATION: Compare strings using only their first 3 characters.
        
        Standard comparison:     if left[i] <= right[j]:
        Substring comparison:    if left[i][:3] <= right[j][:3]:
        
        Args:
            left: First sorted array.
            right: Second sorted array.
            
        Returns:
            A new sorted array containing all elements from both inputs.
        """
        # TODO: Implement merge logic with substring comparison
        # Initialize result = [], i = 0, j = 0
        # While both arrays have elements:
        #   Compare left[i][:3] and right[j][:3]  <-- KEY MODIFICATION
        #   Append smaller element to result
        #   Increment corresponding pointer
        # Append remaining elements from left (if any)
        # Append remaining elements from right (if any)
        # Return result
        raise NotImplementedError


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
    
    test_solution(YourMergeSortSubstring, TEST_CASES, run_case_logic)
