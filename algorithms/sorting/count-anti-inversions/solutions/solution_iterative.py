"""Iterative merge sort solution for counting anti-inversion pairs.

Time complexity: O(n log n) - iterative merge sort with counting
Space complexity: O(n) - temporary arrays during merge
"""

from typing import List


class Solution:
    """Iterative merge sort-based approach to count anti-inversion pairs efficiently."""

    def __init__(self, arr: List[int]):
        """Initialize with the array to analyze.
        
        Args:
            arr: List of integers to count anti-inversions in
        """
        self.arr = list(arr)  # Copy to avoid mutating original

    def count_anti_inversions(self) -> int:
        """Count pairs (i, j) where i < j and arr[i] < arr[j].
        
        Uses iterative merge sort that counts anti-inversions while sorting.
        
        Returns:
            Total count of anti-inversion pairs
        """
        n = len(self.arr)
        if n <= 1:
            return 0
        
        count = 0
        # Create a working copy
        temp = self.arr[:]
        
        # Start with merge subarrays of size 1, then 2, 4, 8, ...
        size = 1
        while size < n:
            # Pick starting index of left sub array to be merged
            for start in range(0, n, size * 2):
                # Find ending point of left subarray
                mid = min(start + size - 1, n - 1)
                # Find ending point of right subarray
                end = min(start + size * 2 - 1, n - 1)
                
                # Merge subarrays arr[start...mid] and arr[mid+1...end]
                if mid < end:
                    merge_count = self._merge(temp, start, mid, end)
                    count += merge_count
            
            # Copy temp back to arr for next iteration
            self.arr = temp[:]
            size *= 2
        
        return count

    def _merge(self, arr: List[int], start: int, mid: int, end: int) -> int:
        """Merge two sorted subarrays and count anti-inversions.
        
        Args:
            arr: Array containing both subarrays
            start: Starting index of left subarray
            mid: Ending index of left subarray
            end: Ending index of right subarray
            
        Returns:
            Count of anti-inversions between the two subarrays
        """
        # Create temporary arrays
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        
        count = 0
        i = j = 0
        k = start
        
        # Merge and count
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                # Count anti-inversions: left[i] < right[m] for all m >= j
                for m in range(j, len(right)):
                    if left[i] < right[m]:
                        count += 1
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
        return count


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
