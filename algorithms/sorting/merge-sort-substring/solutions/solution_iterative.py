"""Iterative (bottom-up) merge sort with substring comparison.

This solution implements merge sort using an iterative approach with
custom substring comparison logic in the merge operation.
"""

from typing import List


class Solution:
    """Iterative (bottom-up) merge sort with substring comparison."""

    def __init__(self, strings: List[str]):
        """Initialize with the list of strings to sort.
        
        Args:
            strings: A list of strings to sort by first 3 characters.
        """
        self.strings = strings

    def merge_sort_substring(self) -> List[str]:
        """Sort strings by their first 3 characters using iterative merge sort.
        
        This bottom-up approach starts with subarrays of size 1 and
        progressively merges adjacent pairs using substring comparison.
        
        Returns:
            A new sorted list of strings.
        """
        # Work with a copy to avoid modifying the original
        arr = self.strings[:]
        n = len(arr)
        
        # Handle edge cases
        if n <= 1:
            return arr
        
        # Start with subarrays of size 1, double the size each iteration
        current_size = 1
        
        while current_size < n:
            # Pick starting index of left subarray to be merged
            left_start = 0
            
            while left_start < n:
                # Find ending point of left subarray
                left_end = min(left_start + current_size - 1, n - 1)
                
                # Find ending point of right subarray
                right_end = min(left_start + 2 * current_size - 1, n - 1)
                
                # Merge subarrays arr[left_start...left_end] and
                # arr[left_end+1...right_end] using substring comparison
                if left_end < right_end:
                    self._merge_in_place(arr, left_start, left_end, right_end)
                
                # Move to next pair of subarrays
                left_start += 2 * current_size
            
            # Double the size for next iteration
            current_size *= 2
        
        return arr
    
    def _merge_in_place(self, arr: List[str], left: int, mid: int, right: int) -> None:
        """Merge two sorted subarrays using substring comparison.
        
        Merges arr[left...mid] and arr[mid+1...right] into a single
        sorted subarray arr[left...right], comparing only the first
        3 characters of each string.
        
        Args:
            arr: The array containing the subarrays.
            left: Starting index of the left subarray.
            mid: Ending index of the left subarray.
            right: Ending index of the right subarray.
        """
        # Create temporary arrays for the two subarrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        # Merge the temporary arrays back into arr[left...right]
        i = j = 0  # Initial indexes of left and right subarrays
        k = left   # Initial index of merged subarray
        
        # KEY MODIFICATION: Compare using first 3 characters
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i][:3] <= right_arr[j][:3]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # Copy remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


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
