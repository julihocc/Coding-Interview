"""Optimized O(n log n) solution using modified merge sort.

Time complexity: O(n log n) - merge sort with counting
Space complexity: O(n) - temporary arrays during merge
"""

from typing import List


class Solution:
    """Merge sort-based approach to count anti-inversion pairs efficiently."""

    def __init__(self, arr: List[int]):
        """Initialize with the array to analyze.
        
        Args:
            arr: List of integers to count anti-inversions in
        """
        self.arr = list(arr)  # Copy to avoid mutating original

    def count_anti_inversions(self) -> int:
        """Count pairs (i, j) where i < j and arr[i] < arr[j].
        
        Uses modified merge sort that counts anti-inversions while sorting.
        During merge, when element from left subarray is taken, it forms
        anti-inversion pairs with all remaining elements in right subarray.
        
        Returns:
            Total count of anti-inversion pairs
        """
        _, count = self._merge_sort_and_count(self.arr, 0, len(self.arr) - 1)
        return count

    def _merge_sort_and_count(self, arr: List[int], left: int, right: int) -> tuple[List[int], int]:
        """Recursively sort and count anti-inversions.
        
        Args:
            arr: Array to sort
            left: Left boundary index
            right: Right boundary index
            
        Returns:
            Tuple of (sorted_subarray, anti_inversion_count)
        """
        if left >= right:
            return [arr[left]] if left == right else [], 0
        
        mid = (left + right) // 2
        
        # Recursively count in left and right halves
        left_sorted, left_count = self._merge_sort_and_count(arr, left, mid)
        right_sorted, right_count = self._merge_sort_and_count(arr, mid + 1, right)
        
        # Merge and count cross-inversions
        merged, merge_count = self._merge_and_count(left_sorted, right_sorted)
        
        total_count = left_count + right_count + merge_count
        return merged, total_count

    def _merge_and_count(self, left: List[int], right: List[int]) -> tuple[List[int], int]:
        """Merge two sorted arrays and count anti-inversions.
        
        When we take an element from the left array that is strictly less
        than elements in the right array, it forms anti-inversions.
        
        Args:
            left: Sorted left subarray
            right: Sorted right subarray
            
        Returns:
            Tuple of (merged_sorted_array, anti_inversion_count)
        """
        merged = []
        count = 0
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                # Count anti-inversions: left[i] < right[k] for all k >= j
                # Only count when strictly less than
                for k in range(j, len(right)):
                    if left[i] < right[k]:
                        count += 1
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Add remaining elements
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged, count


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
        instance = SolutionClass(list(case.arr))
        result = instance.count_anti_inversions()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
