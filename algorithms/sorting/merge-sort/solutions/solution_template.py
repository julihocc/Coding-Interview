"""TEMPLATE: Class-based solution for Merge Sort

Implement a class whose name reflects the strategy (e.g., RecursiveMergeSort).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class YourMergeSort:
    """Rename and implement this class to match your approach.
    
    Example strategies: NaiveSorter, RecursiveMergeSort, IterativeMergeSort
    """

    def __init__(self, nums: List[int]):
        """Initialize with the array to sort.
        
        Args:
            nums: An unsorted list of integers.
        """
        self.nums = nums

    def merge_sort(self) -> List[int]:
        """Sort self.nums and return the sorted array.
        
        Expected behavior:
        - Return a sorted version of self.nums
        - Handle edge cases: empty, single element, duplicates
        - Maintain stability (equal elements keep relative order)
        
        Approaches to consider:
        1. Naive: Use Python's built-in sorted() function
        2. Recursive: Divide array in half, recursively sort, then merge
        3. Iterative: Bottom-up approach merging progressively larger subarrays
        
        Returns:
            A sorted list containing all elements from self.nums.
        """
        # TODO: Implement your sorting strategy
        # For recursive approach: call _merge_sort_recursive(self.nums)
        # For iterative approach: use a loop with progressively larger merge sizes
        # For naive approach: return sorted(self.nums)
        raise NotImplementedError
    
    def _merge_sort_recursive(self, arr: List[int]) -> List[int]:
        """Recursively sort an array using merge sort.
        
        Divide-and-conquer approach:
        1. Base case: arrays with 0 or 1 elements are already sorted
        2. Divide: split array at midpoint
        3. Conquer: recursively sort both halves
        4. Combine: merge the sorted halves
        
        Args:
            arr: The array to sort.
            
        Returns:
            A new sorted array.
        """
        # TODO: Implement recursive merge sort
        # Base case: if len(arr) <= 1, return arr
        # Find mid = len(arr) // 2
        # Recursively sort left = arr[:mid] and right = arr[mid:]
        # Return _merge(left, right)
        raise NotImplementedError
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays into a single sorted array.
        
        Use two pointers to compare elements from both arrays and
        build the result in sorted order.
        
        Args:
            left: First sorted array.
            right: Second sorted array.
            
        Returns:
            A new sorted array containing all elements from both inputs.
        """
        # TODO: Implement merge logic
        # Initialize result = [], i = 0, j = 0
        # While both arrays have elements:
        #   Compare left[i] and right[j]
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
        instance = SolutionClass(list(case.nums))
        result = instance.merge_sort()
        return result == case.expected
    
    test_solution(YourMergeSort, TEST_CASES, run_case_logic)
